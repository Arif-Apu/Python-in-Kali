
'''
Caesar Cipher Technique is the simple and easy method of encryption technique.

It is simple type of substitution cipher. Each letter of plain text is replaced or shifted by a letter with some fixed number of positions.
For example, with a shift of 1, A would be replaced by B, B would become C, and so on. 
'''

#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Usage: python caesar.py -k <Key> -m <Message> -M <Mode>")
parser.add_argument("-k", "--key", dest="Key", help="Enter the key value")
parser.add_argument("-m", "--message", dest="Message", help="Enter your Message")
parser.add_argument("-M", "--MODE", dest="Mode", help="Enter the Mode")
parsed_args = parser.parse_args()
if parsed_args.Key is None:
    print("[-] Enter a key value, -h or --help for more")
if parsed_args.Message is None:
    print("[-] Enter your secret message, -h or --help for more")
if parsed_args.Mode is None:
    print("[-] Enter the mode encrypt or decrypt, -h or --help for more")

Key = parsed_args.Key
Message = parsed_args.Message
Mode = parsed_args.Mode
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
Message = Message.upper()

for symbol in Message:
    if symbol in letters:
        num = letters.find(symbol)
        if Mode == 'encrypt':
            num = num + int(Key)
        elif Mode == 'decrypt':
            num = num - int(Key)

        if num >= len(letters):
                num = num - len(letters)
        elif num < 0:
            num = num + len(letters)
        translated = translated + letters[num]

    else:
        translated = translated + symbol
try:
    print("\nThe Encrypted/Decrypted Message is: " + translated)
except:
    pass





