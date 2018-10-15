# [CSE Puzzle Challenge - Puzzle 3](https://www.cse-cst.gc.ca/en/puzzles-enigmes/puzzle-enigme-3)

The challenge is quite fun and can drive you crazy quite easily if you don't take the time to test every simple possibilities first.

The solution is already [here](https://www.cse-cst.gc.ca/en/puzzles-enigmes/puzzle-enigme-3-solution), but the knightDecoding.py is not released yet (2018-10-24).

I didn't solve it entirely, because I had university, but friends of mine asked me how I did the first part.

Here is one way of doing it with my knightDecoding.py version [](/knights.py) using [pillow](https://pillow.readthedocs.io/) in Python.

## The story
The first part is quite easy when you think about it. There are four knights directions. It has to be translated to something understandable by human like us. Let's try base 4.
Mathematically, there are 24 possibilities, and because there is no way to tell if direction (BACK, FRONT, RIGHT, LEFT) has the value 0 or 1 or 2 or 3, bruteforce must come to the rescue.

Using the script above, you end up with the following message:

```text
Forsyth & Edwards need a checkmate next move: 3n4/k1P2P1p/3Q2p1/p7/K3Bb1r/P7/5P2/1q6 w - - 0 1 | pass=md5(winning_fen)
```

The directions end up to be `BACK = 2`, `FRONT = 0`, `RIGHT = 1` and `LEFT = 3`.

The rest of the puzzle is well described in their [solution](https://www.cse-cst.gc.ca/en/puzzles-enigmes/puzzle-enigme-3-solution) and it will make you want to play chess :D

For binwalk, here is how I did it:

```text
$ binwalk knights.jpg
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
1335707       0x14619B        Zip archive data, encrypted at least v2.0 to extract, compressed size: 467264, uncompressed size: 468062, name: A
1803046       0x1B8326        Zip archive data, encrypted at least v2.0 to extract, compressed size: 476864, uncompressed size: 477736, name: B
2280127       0x22CABF        End of Zip archive

$ dd if=knights.jpg bs=1 skip=1335707 count=2280127 of=knights.zip
944442+0 records in
944442+0 records out
944442 bytes (944 kB, 922 KiB) copied, 1.25487 s, 753 kB/s

$ unzip -P e818b1db90db15f2f86cb768481c6da9 knights.zip
Archive:  knights.zip
[knights.zip] A password:
  inflating: A              
  inflating: B
```

## Mistakes I did
Never assume something. Since, I didn't know which values go to which directions, I assumed that BACK (or UP) = 0, FRONT (or DOWN) = 1, RIGHT = 2, LEFT = 3 assuming cardinality directions encoding such that north, south, east and west were respectively 0, 1, 2, 3. It will give: `´·²¹EHE»´·EEE¹E±¹E¸pEwyOv¥t¥vµOw¦tµvOµ{Owv´O¥{Oz¥tOv¶xE»ENENEuEvE½Eµ··~zA»¯BEE`. That is not smart at all. Instead, test every possibilities.

## Last words
Thanks CSE! Good job! ;o
