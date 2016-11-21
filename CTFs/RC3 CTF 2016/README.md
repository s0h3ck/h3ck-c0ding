# RC3 CTF 2016 writeup

## Crypto 100
Category: Crypto Points: 100 Solves: Description:

<blockquote>
7sj-ighm-742q3w4t

Partial missing.
</blockquote>

## Write-up

TODO

A slight modification of the standard caesar cipher.

```text
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
KLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJ 

7sj-ighm-742q3w4t
RC3-2016-ROMANGOD
```

The flag is 
`=> RC3-2016-ROMANGOD`

## Crypto 200
Category: Crypto Points: 200 Solves: Description:

<blockquote>
Missing.
</blockquote>

## Write-up
TODO

A bunch of equations, just take the variable name : `A-N-T-I-D-E-R-V`

The flag is
`=> RC3-2016-ANTIDERV`

## Crypto 300
Category: Crypto Points: 300 Solves: Description:

<blockquote>
Missing.
</blockquote>

## Write-up
The idea is to count the number of cats in each slide and then convert it to ASCII caracters and reverse it to get the flag.

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

The flag is
`=> RC3-2016-MEOWTAIN`

Thanks @Neolex for giving me this suggestion.

## Crypto 400
Category: Crypto Points: 400 Solves: Description:

<blockquote>
Letters intertwined
The end, recombined.
Awake, lying blinking,
Intensely thinking.
Muse and proclaim...
“It’s my game!”

?HLJ1>AA"AII>888!CE9>AA>"~>IIG888BAA~@>d>B~B?
HH0bAI>>AE&>IIAACMQa
</blockquote>

## Write-up
Coming soon... but here is the idea

1. Get the clue
`LiTerAlbItMapImg => literal bitmap img`
2. Convert the ASCII caracteres in binary

```text
00111111 01001000 01001100 01001010 00110001 00111110 01000001 01000001 00100010 01000001 01001001 01001001 00111110 00111000 00111000 00111000 00100001 01000011 01000101 00111001 00111110 01000001 01000001 00111110 00100010 01111110 00111110 01001001 01001001 01000111 00111000 00111000 00111000 01000010 01000001 01000001 01111110 01000000 00111110 01100100 00111110 01000010 01111110 01000010 00111111 01001000 01001000 00110000 01100010 01000001 01001001 00111110 00111110 01000001 01000101 00100110 00111110 01001001 01001001 01000001 01000001 01000011 01001101 01010001 01100001
```

Total of 65 caracteres.

3. Wrote a script to do a .pbm bitmap

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

4. Open the image and voilà!

The flag is
`=> RC3-2016-JAIP3GEZ`

It sounds likes a French expression : `j'ai pigé` ;p
