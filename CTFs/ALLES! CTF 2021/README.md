# ALLES! CTF 2021 

## Pyimplant
**Category:** Misc
**Points:**
**Solves:** 
**Description:**

> "Our company just developed an awesome python TicTacToe game. Before shipping, it was compiled to bytecode to minimize size and enable a faster download all over the world. However, in the recent days we found a version of our bytecode online, which produces another sha256sum as our original one, but it still works properly and has all our fancy features!? What did they manipulate? Can you find any implants?

> You'll find the source code and the manipulated version attached in the ZIP file."

## Write-up
Easy challenge. Linux Fu only! Challenge accepted! :D

```console
➜ unzip pyimplant.zip 
Archive:  pyimplant.zip
   creating: pyimplant/
  inflating: pyimplant/manipulated_tictactoe.cpython-36.pyc  
  inflating: pyimplant/tictactoe.py  
```

```console
➜ mkvirtualenv ctf_py36 -p python3.6
[...]
(ctf_py36) ➜ cd pyimplant/
(ctf_py36) ➜ python -m compileall tictactoe.py
Compiling 'tictactoe.py'...
(ctf_py36) ➜ cp __pycache__/tictactoe.cpython-36.pyc .
```

The idea is to compare the bytes that are different using the command `cmp`.

`cmp -l manipulated_tictactoe.cpython-36.pyc tictactoe.cpython-36.pyc`

Next, convert to hexadecimal using the command `gawk`.

`gawk '{printf "%08X %02X %02X\n", $1, strtonum(0$2), strtonum(0$3)}`

Next, transpose the columns to rows. Very handy reference : [Rows to column conversion of file](https://unix.stackexchange.com/questions/169995/rows-to-column-conversion-of-file)

`awk '{ for (i=1; i<=NF; i++) RtoC[i]= (RtoC[i]!=""? RtoC[i] FS $i: $i) } END{ for (i in RtoC) print RtoC[i] }'`

Then, filter the bytes to those observed in the manipulated file.

`head -n 2`

Finally, convert the hexadecimal to ascii. 

`xxd -r -p | strings | grep "ALLES"`

One line command : `cmp -l manipulated_tictactoe.cpython-36.pyc tictactoe.cpython-36.pyc | gawk '{printf "%08X %02X %02X\n", $1, strtonum(0$2), strtonum(0$3)}' | awk '{ for (i=1; i<=NF; i++) RtoC[i]= (RtoC[i]!=""? RtoC[i] FS $i: $i) } END{ for (i in RtoC) print RtoC[i] }' | head -n 2 | xxd -r -p | strings | grep "ALLES"`

Looks simple! Huh? :D

The flag is `ALLES!{py7h0n_byt3cod3_s3cr3ts}`
