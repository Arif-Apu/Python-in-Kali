
#!/usr/bin/env python

import requests
import re
import urlparse

'''
https://docs.python.org/3/library/urllib.parse.html?highlight=urlparse
urlparse — Parse URLs into components. This module defines a standard interface to break Uniform Resource Locator (URL) 
strings up in components (addressing scheme, network location, path etc.), to combine the components back into a URL string, 
and to convert a relative URL to an absolute URL given a base URL.

https://docs.python.org/3/library/re.html?highlight=re#module-re
A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check if a 
particular string matches a given regular expression (or if a given regular expression matches a particular string, which 
comes down to the same thing).
'''

target_url = input("\nEnter Target URL inside Single or Double Quotation marks: \n\nTarget URL --> ")
target_links = []


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)





