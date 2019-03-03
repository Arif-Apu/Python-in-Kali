
'''

Caesar Cipher Technique is the simple and easy method of encryption technique.

It is simple type of substitution cipher. Each letter of plain text is replaced or shifted by a letter with some fixed number of positions.
For example, with a shift of 1, A would be replaced by B, B would become C, and so on. 

'''

#!/usr/bin/env python


key = input('\nEnter the key: ')

message = input('\nEnter the Message inside Single or Double Quotation marks: \n')

mode = input('\nEnter the mode(encrypt/decrypt) inside Single or Double Quotation marks: \n')
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

message = message.upper()

for symbol in message:
    if symbol in letters:
        num = letters.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(letters):
            num = num - len(letters)
        elif num < 0:
            num = num + len(letters)
        translated = translated + letters[num]

    else:
        translated = translated + symbol

print("\nThe Encrypted/Decrypted Message is: " + translated)





