

#!/usr/bin/env python

import requests
import optparse

'''
http://docs.python-requests.org/en/master/
The requests library is the de facto standard for making HTTP requests in Python. It abstracts the complexities of making 
requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your 
application.
Requests will allow you to send HTTP/1.1 requests using Python. With it, you can add content like headers, form data, 
multipart files, and parameters via simple Python libraries. It also allows you to access the response data of Python
in the same way.

https://docs.python.org/3/library/optparse.html?highlight=optparse#module-optparse
optparse is a more convenient, flexible, and powerful library for parsing command-line options.
optparse uses a more declarative style of command-line parsing.

'''

def request(URL):
    try:
        return requests.get(URL)
    except requests.exceptions.ConnectionError:
        pass
    
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="URL", help="Target url to find ")
    (options, arguments) = parser.parse_args()
    if not options.URL:
        parser.error("[-] Please specify an URL, -h or --help for more")
    return options

def finding_subdomain(URL):
    with open("/root/subdomain.txt", "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            test_url = URL + "/" + word
            response = request(test_url)
            if response:
                print("[+] Discovering URL --> " + test_url)
                

try:
    options = get_arguments()
    finding_subdomain(options.URL)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL +C ... \n")



            
