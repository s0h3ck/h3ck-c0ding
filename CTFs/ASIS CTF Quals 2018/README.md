# ASIS CTF Quals 2018

## The Early School 
**Category:** Crypto
**Points:** 32
**Solves:** 210
**Description:**

> Welcome to ASIS Early School.

## Write-up
The idea is to write a decrypt function. The logic to encrypt the data is given a string, for each two bits, you take the 2 bits and you concatenate these two bits with the result of the xor of these two bits. Then, you concatenate all the pieces of 3 bits and so on. There is also a variable round you can specify to repeate this process a certain number of times.

Here is the logic:
```
00 -> 001
01 -> 010
10 -> 100
11 -> 111
```

We know that each flag starts with 'ASIS', so we could get the minimum layer of encryption `1000001010100110100100101010011`.

Know, we know all the pieces, we write our decrypt function and do the reverse process back to the first layer of encryption.

```python
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
        # 18 rounds
        break

# Since the flag start with 'A' we have 7 bits, we need to add '0b0' to convert it from bin to ascii
binary_flag = '0b0' + data

# print("Binary flag:", binary_flag)

def decode_binary_string(s): # from stackoverflow
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

ascii_flag = decode_binary_string(binary_flag[2:])

print("Flag:", ascii_flag)
```

The flag is `=> ASIS{50_S1mPl3_CryptO__4__warmup____}`
