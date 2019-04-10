

#!/usr/bin/env python


import requests
import argparse

'''
http://docs.python-requests.org/en/master/
The requests library is the de facto standard for making HTTP requests in Python. It abstracts the complexities of making 
requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your 
application.
Requests will allow you to send HTTP/1.1 requests using Python. With it, you can add content like headers, form data, 
multipart files, and parameters via simple Python libraries. It also allows you to access the response data of Python
in the same way.

https://docs.python.org/3/library/argparse.html?highlight=argparse#module-argparse
The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments 
it requires, and argparse will figure out how to parse those. 

'''

parser = argparse.ArgumentParser(description="\n[+] Usage: python spider.py -u <url> -w <word_file>  or --help for more")
parser.add_argument("-u", "--url", dest="URL", help="specify the target url")
parser.add_argument("-w", "--wordfile", dest="WFILE", help="specify a wordfile")
parsed_args = parser.parse_args()
if parsed_args.URL is None:
    parser.error("[-] Please specify an url, -h or --help for more")
if parsed_args.WFILE is None:
    parser.error("[-] Please specify a word_file, -h or --help for more")
    
try:
    URL = parsed_args.URL
    WFILE = parsed_args.WFILE

except:
    print(parser.description)
    exit(0)

with open(WFILE, "r") as word_file:
    try:
        for line in word_file:
            word = line.strip()
            test_url = URL + "/" + word
            response = requests.get(test_url)
            if response:
                print("[+] Discovering URL ---> " + test_url)
    except KeyboardInterrupt:
        print("\n[-] Detected CTRL+C ....\n")




            
