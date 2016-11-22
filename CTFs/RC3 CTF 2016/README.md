# RC3 CTF 2016 writeup

## Salad
**Category:** Crypto
**Points:** 100
**Solves:** 
**Description:**

> “The fault, dear Brutus, is not in our stars, but in ourselves.” (I.ii.141) Julius Caesar in William Shakespeare’s Julius Caesar

> Cipher Text: 7sj-ighm-742q3w4t

## Write-up
The idea behind this problem is to find out which cipher is. In each CTF, it's pretty common to have a subtitution cipher. No doubt, I though it would be the Caesar cipher, but the first half (almost each challenge) had `RC3-2016-` so, the substitution cipher must handle the number as well.

A slight modification of the standard Caesar cipher give us a equivalent to a right shift of 20.

```text
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
KLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJ 

7sj-ighm-742q3w4t
RC3-2016-ROMANGOD
```

The flag is `=> RC3-2016-ROMANGOD`

## Calculus
**Category:** Crypto
**Points:** 200
**Solves:** 
**Description:**

> Missing. There was a shared Google document link in view mode.

## Write-up
A bunch of equations, just take one variable name of each equation and concatenate them : `A-N-T-I-D-E-R-V`

The flag is `=> RC3-2016-ANTIDERV`

## Cats
**Category:** Crypto
**Points:** 300
**Solves:** 
**Description:**

> Missing.

## Write-up
The idea is to count the number of cats in each slide and then convert it to alphabetic letter and reverse it to get the flag.

```text
Image 1: 14 cats - N
Image 2:  9 cats - I
Image 3:  1 cat  - A
Image 4: 20 cats - T
Image 5: 23 cats - W
Image 5: 15 cats - O
Image 6:  5 cats - E
Image 7: 13 cats - M

NIATWOEM
MEOWTAIN
```

The flag is `=> RC3-2016-MEOWTAIN`

Thanks @Neolex for giving me this suggestion.

## My Game
**Category:** Crypto
**Points:** 400
**Solves:** 
**Description:**

> *Letters intertwined*  
> *The end, recombined.*  
> *Awake, lying blinking,*  
> *Intensely thinking.*  
> *Muse and proclaim...*  
> *“It’s my game!”*  
>
> ?HLJ1>AA"AII>888!CE9>AA>"~>IIG888BAA~@>d>B~B?  
> HH0bAI>>AE&>IIAACMQa

## Write-up
After hours of searching and trying and...  (╯°□°)╯︵ ┻━┻, I decided to note the first letter of each word 

> **L**etters **i**ntertwined  
> **T**he **e**nd, **r**ecombined.  
> **A**wake, **l**ying **b**linking,  
> **I**ntensely **t**hinking.  
> **M**use **a**nd **p**roclaim...  
> “**I**t’s **m**y **g**ame!”

Oh... ┐(°‿°)┌ , we got `LiTerAlbItMapImg => literal bitmap img`, coincidence? No!

After some digging on the Internet and old experience with pgm and ppm at my University, I found out that the best way to represent the data `?HLJ1>AA"AII>888!CE9>AA>"~>IIG888BAA~@>d>B~B?HH0bAI>>AE&>IIAACMQa` was to use the format pbm. So, I [converted](http://www.asciitohex.com/) it, which turns out to be 

```text
00111111 01001000 01001100 01001010 00110001 00111110 01000001 01000001 00100010 01000001 01001001 01001001 00111110 00111000 00111000 00111000 00100001 01000011 01000101 00111001 00111110 01000001 01000001 00111110 00100010 01111110 00111110 01001001 01001001 01000111 00111000 00111000 00111000 01000010 01000001 01000001 01111110 01000000 00111110 01100100 00111110 01000010 01111110 01000010 00111111 01001000 01001000 00110000 01100010 01000001 01001001 00111110 00111110 01000001 01000101 00100110 00111110 01001001 01001001 01000001 01000001 01000011 01001101 01010001 01100001
```
Total of 65 characteres.

Before we write a script in the format of pbm, we need to know the width and height of the bitmap. Above, the data give us 65 bytes, so the more appropriate way to represent it horizontally is to have 65 bits by 8 bits.

I wrote my script and I got the desired portable bitmap. For more information about bitmap format, [click here](https://en.wikipedia.org/wiki/Netpbm_format). 

```python
import sys

WIDTH  = 65
HEIGHT = 8

pixel_flag = [[0 for i in range(WIDTH)] for j in range(HEIGHT)] 

file = open("binary.txt", "r")

binary_line = file.readline()

y = 0
x = 0
for binary in binary_line:
    
    if binary != '1' and binary != '0' and binary != ' ':
        break

    if binary == ' ':
        x += 1
        y = 0
    else:
        pixel_flag[y][x] = binary
        y += 1

file.close()

file = open("flag-crypto400.pbm", "w+")

file.write('P1\n')
file.write('65 8\n')
for i in range(HEIGHT):
    for j in range(WIDTH):
        file.write(str(pixel_flag[i][j]))
    file.write('\n')
file.close()
```

At last, the dreadful part is to open the image and voilà!

![alt text](https://github.com/s0h3ck/h3ck-c0ding/edit/master/CTFs/RC3%20CTF%202016/flag-crytpo400.png "RC3-2016-JAIP3GEZ")

The flag is `=> RC3-2016-JAIP3GEZ`

It sounds like a French expression : `j'ai pigé` ;p

### Last words
A big thanks to RC3-2016 Team. It was really fun :)
