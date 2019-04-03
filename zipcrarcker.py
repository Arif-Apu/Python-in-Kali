
!/usr/bin/ env python

from zipfile import ZipFile
import argparse

'''
https://docs.python.org/2/library/zipfile.html?highlight=zipfile#module-zipfile
The ZIP file format is a common archive and compression standard. This module provides tools to create, read, write, 
append, and list a ZIP file.
'''

parser = argparse.ArgumentParser(description="\nUsage: python zipcracker.py -z <zipfile> -p <passwordfile>")
parser.add_argument("-z", dest="ziparchive",help="Zip Archive file")
parser.add_argument("-p", dest="passfile", help="Password File")
parsed_args = parser.parse_args()
if parsed_args.ziparchive is None:
    parser.error("[-] Please specify a Zipfile, -h or --help for more")


try:
    ziparchive = ZipFile(parsed_args.ziparchive)
    passfile = parsed_args.passfile
    foundpass = ""

except:
    print(parser.description)
    exit(0)

with open(passfile, "r") as word_file:
    for line in word_file:
        password = line.strip()
        password = password.encode()

        try:
            foundpass = ziparchive.extractall(pwd=password)
            if foundpass is None:
                print("\n[+] Got The Password--> " + password + "\n")

        except RuntimeError:
            pass

    if foundpass == "":
        print("\n[-] Password Not Found")
        
        
        
        
        
        
