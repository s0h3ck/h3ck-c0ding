import sys

WIDTH  = 65
HEIGHT = 8

pixel_flag = [[0 for i in range(WIDTH)] for j in range(HEIGHT)] 

for i in range(HEIGHT):
    for j in range(WIDTH):
        sys.stdout.write(str(pixel_flag[i][j]))
    print(' ')

file = open("binary.txt", "r")
binary_line = file.readline()

print(binary_line)

y = 0
x = 0
for binary in binary_line:
    
    if binary != '1' and binary != '0' and binary != ' ':
        print('boom')
        break

    if binary == ' ':
        print('pah')
        x += 1
        y = 0
    else:
        print('['+str(x)+']['+str(y)+'] = '+str(binary))
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
