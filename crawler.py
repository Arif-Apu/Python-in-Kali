


#!/usr/bin/env python

import requests
import re
import urlparse
import optparse


'''
https://docs.python.org/3/library/urllib.parse.html?highlight=urlparse
Parse URLs into components. This module defines a standard interface to break Uniform 
Resource Locator (URL) strings up in components (addressing scheme, network location, path etc.), 
to combine the components back into a URL string, and to convert a relative URL to an absolute URL 
given a base URL.

https://docs.python.org/3/library/re.html?highlight=re#module-re
A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let 
you check if a particular string matches a given regular expression (or if a given regular expression 
matches a particular string, which comes down to the same thing).

https://docs.python.org/3/library/optparse.html?highlight=optparse#module-optparse
optparse is a more convenient, flexible, and powerful library for parsing command-line options.
optparse uses a more declarative style of command-line parsing.

http://docs.python-requests.org/en/master/
Requests is an elegant and simple HTTP library for Python, used to send HTTP request.
'''

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="URL", help="Target url to crawl")
    (options, arguments) = parser.parse_args()
    if not options.URL:
        parser.error("[-] Please specify an URL, -h or --help for more")
    return options

target_links = []


def extract_links_from(URL):
    response = requests.get(URL)
    return re.findall('(?:href=")(.*?)"', response.content)

def target(URL):
        print("[+] Crawling " + URL)

def crawl(URL):
    href_links = extract_links_from(URL)
    for link in href_links:
        link = urlparse.urljoin(URL, link)

        if "#" in link:
            link = link.split("#")[0]

        if URL in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

try:
    options = get_arguments()
    target(options.URL)
    crawl(options.URL)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL +C ... Cannot crawling \n")






