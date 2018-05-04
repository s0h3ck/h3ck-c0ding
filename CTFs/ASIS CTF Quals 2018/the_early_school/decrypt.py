#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Util.number import *

ASIS_FLAG = "1000001010100110100100101010011"

def decrypt(msg):
    dec = []
    for i in range(0, len(msg), 3):
        dec.append(msg[i:i+2])

    return ''.join(dec)

with open('FLAG.enc', 'rb') as f:
  content = f.read()

data = bin(bytes_to_long(content))[2:]

for _ in range(256):
    data = decrypt(data)
    if data.startswith(ASIS_FLAG):
        # print(_)
        break

# Since the flag start with 'A' we have 7 bits, we need to add '0b0' to convert it from bin to ascii
binary_flag = '0b0' + data

# print("Binary flag:", binary_flag)

def decode_binary_string(s): # from stackoverflow
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

ascii_flag = decode_binary_string(binary_flag[2:])

print("Flag:", ascii_flag)

