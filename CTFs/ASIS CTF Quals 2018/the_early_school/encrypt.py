#!/usr/bin/python

from Crypto.Util.number import *
#from flag import FLAG, round

FLAG = "ASIS".encode()
round = 8

def encrypt(msg):
    assert set(msg) == set(['0', '1'])
    print(msg)
    enc = []
    for i in range(0, len(msg), 2):
        a = msg[i:i+2]
        b = str(int(msg[i]) ^ int(msg[min(i+1, len(msg)-1)]))
        #print(a,b,a+b,'|',end='')
        enc.append(a + b)

    #print(enc)
    return ''.join(enc)

ENC = bin(bytes_to_long(FLAG))[2:]
print(bin(bytes_to_long(FLAG)))
print(ENC)

for _ in range(2):
    ENC = encrypt(ENC)


