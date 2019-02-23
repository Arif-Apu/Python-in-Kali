
#!/usr/bin/env python
#Source: https://scapy.readthedocs.io/en/latest/installation.html
#Source: https://github.com/secdev/scapy
#from scapy.all import *

import scapy.all as scapy
import argparse

'''
Python argparse module is the preferred way to parse command line arguments. Parsing command-line arguments is a very common 
task, which Python scripts do and behave according to the passed values. 
'''

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Specify Target IP/IP Range: example, 192.168.2.1/24")
    options = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address")
    print("------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)




