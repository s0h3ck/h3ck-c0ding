import sys
import itertools

from PIL import Image

im = Image.open("knights_cropped.jpg")

WIDTH, HEIGHT = im.size

# 2816 * 1755
# 32 * 15
# 88 * 117

PIECES_WIDTH = 32
PIECES_HEIGHT = 15

PIECES_WIDTH_PIXEL = WIDTH // PIECES_WIDTH
PIECES_HEIGHT_PIXEL = HEIGHT // PIECES_HEIGHT

#print(WIDTH, HEIGHT)
#print(PIECES_WIDTH_PIXEL)
#print(PIECES_HEIGHT_PIXEL)

# Functions

def average_image(width, height, image):
    total = 0
    for i in range(0, width):
        for j in range(0, height):
            total += image.getpixel((i,j))[0]

    mean = total / (width * height)
    return mean

def display_grid(grid):
    for line in grid:
        print(line)

for i in [(2, 0, 1, 3)]: #itertools.permutations([0, 1, 2, 3]):
    BACK, FRONT, RIGHT, LEFT = list(i)

    grid = [[0 for x in range(PIECES_WIDTH)] for y in range(PIECES_HEIGHT)]

    for i in range(0, PIECES_WIDTH):
        for j in range(0, PIECES_HEIGHT):

            left = i * PIECES_WIDTH_PIXEL
            top = j * PIECES_HEIGHT_PIXEL
            right = (i + 1) * PIECES_WIDTH_PIXEL
            bottom = (j + 1) * PIECES_HEIGHT_PIXEL

            area = (left, top, right, bottom)

            #print(area)
            t = im.crop(area)

            piece = t.crop((25, 23, 88-25, 117-10))
            head = t.crop((25, 23, 88-25, 117-71))

            piece_average = int(average_image(37, 84, piece))
            head_average = int(average_image(37, 23, head))

            side = False
            threadhold_side = 233
            if head_average < threadhold_side:
                side = True

            if side:
                #print("SIDE", end = ' ')
                #print(head_average, end=' ')
                threadhold_right = 215
                if piece_average < threadhold_right:
                    #print("LEFT", end=' ')
                    grid[j][i] = LEFT
                else:
                    #print("RIGHT", end=' ')
                    grid[j][i] = RIGHT
                #print(piece_average)
            else:
                #print("FACE", end = ' ')
                #print(head_average, end=' ')
                threadhold_front = 223
                if piece_average > threadhold_front:
                    #print("FRONT", end = ' ')
                    grid[j][i] = FRONT
                else:
                    #print("BACK", end = ' ')
                    grid[j][i] = BACK
                #print(piece_average)

    # display_grid(grid)

    base = 4
    for line in grid:
        for values_tuple in zip(*[iter(line)]*base):
            character = ''.join(str(i) for i in values_tuple)
            character = int(character, base)
            print(chr(character), end='')

    print("B={}, F={}, R={}, L={}".format(BACK, FRONT, RIGHT, LEFT))
