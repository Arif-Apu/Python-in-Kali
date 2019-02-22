
#!usr/bin/env python

import requests

'''
The requests library is the de facto standard for making HTTP requests in Python. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application.

Requests will allow you to send HTTP/1.1 requests using Python. With it, you can add content like headers, form data, multipart files, and parameters via simple Python libraries. It also allows you to access the response data of Python in the same way.

'''


def request(url):
    try:
        return requests.get("http://" + url)
        #print(get_response)
    except requests.exceptions.ConnectionError:
        pass


target_url = "example.com"
with open("/root/common.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovering URL --> " + test_url)

