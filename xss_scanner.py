
#!/usr/bin/ env python


import requests
import urlparse
import re
from BeautifulSoup import BeautifulSoup


'''
https://pypi.org/project/beautifulsoup4/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
The Fish-Footman began by producing from under his arm a great letter, nearly as large as himself.
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite 
parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.

https://docs.python.org/3/library/re.html?highlight=re#module-re
A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check 
if a particular string matches a given regular expression

https://docs.python.org/3/library/urllib.parse.html?highlight=urlparse
This module defines a standard interface to break Uniform Resource Locator (URL) strings up in components 
(addressing scheme, network location, path etc.), to combine the components back into a URL string, and to convert 
a relative URL to an absolute URL given a base URL.

http://docs.python-requests.org/en/master/
'''

class Scanner:
    def __init__(self, url): 
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []
        

    def extract_links_from(self, url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', response.content)

    def crawl(self, url=None):
        if url == None:
            url = self.target_url
        href_links = self.extract_links_from(url)
        for link in href_links:
            link = urlparse.urljoin(url, link)

            if "#" in link:
                link = link.split("#")[0]

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)

    def extracts_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content)
        return parsed_html.findAll("form")

    def submit_form(self, form, value, url):
        action = form.get("action")
        post_url = urlparse.urljoin(url, action)
        method = form.get("method")

        input_list = form.findAll("input")
        post_data = {}
        for input in input_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")
            if input_type == "text":
                input_value = value

            post_data[input_name] = input_value
            if method == "post":
                return self.session.post(post_url, data=post_data)
            return self.session.get(post_url, params=post_data)

    def run_scanner(self):
        for link in self.target_links:
            forms = self.extracts_forms(link)
            for form in forms:
                print("[+] Testing form in " + link)
                is_vulnerable_to_xss = self.test_xss_in_form(form, link)
                if is_vulnerable_to_xss:
                    print("\n\n[***] Discovered XSS " + link + "in the following")
                    print(form)

            if "=" in link:
                print("\n\n[+] Testing " + link)
                is_vulnerable_to_xss = self.test_xss_in_link(link)
                if is_vulnerable_to_xss:
                    print("[***] Discovered XSS in " + link)

    def test_xss_in_link(self, url):
        xss_test_script = "<script>alert('XSS')</script>"
        url = url.replace("=", "=" + xss_test_script)
        response = self.session.get(url)
        return xss_test_script in response.content

    def test_xss_in_form(self, form, url):
        xss_test_script = "<script>alert('Test')</script>"
        response = self.submit_form(form, xss_test_script, url)
        return xss_test_script in response.content


'''
In order to use this class Scanner, create an object that uses the blueprint or code to work.
Create a seperate python file, name it like xss_scanner.py and run this file. This file is actually to be the file that
uses this object and runs scanner.py
'''


#!/usr/bin/env python


import scanner


target_url = "http://192.168.1.10/dvwa"
vuln_scanner = scanner.Scanner(target_url)
vuln_scanner.crawl()
vuln_scanner.run_scanner()





