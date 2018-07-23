import socket

from itertools import product
from itertools import combinations

from time import sleep

def do_the_magic_for_me(values, answer):
    l_v = len(values)
    possible_position = l_v - 1
    
    apsc = []
    for i in combinations([i for i in range(0, l_v)],2):
        apsc.append(list(i))

    for i in range(-1,l_v-1):
        for j in combinations(apsc, i+1):
            l = list(j)

            take = values[:]
            for sp in l:
                take[sp[0]] = '(' + take[sp[0]]
                take[sp[1]] = take[sp[1]] + ')'

            take_frame = ' '.join(take)
            number_of_space = l_v - 1

            for i in product(operators, repeat=number_of_space):
                equation = take_frame
                for j in range(0, number_of_space):
                    equation = equation.replace(' ', i[j], 1)
                
                try:
                    r = eval(equation)

                    if str(r) == answer:
                        return equation
                except:
                    pass

s = socket.socket()
s.connect(("ppc-01.v7frkwrfyhsjtbpfcppnu.ctfz.one", 2445))

operators = ['+', '*', '-', '/']

for i  in range(24):
    result = s.recv(1024).decode("utf-8")
    numbers = result.rstrip('\n').split(' ')
    
    l = len(numbers)
    
    values = numbers[:l-1]
    answer = numbers[l-1]
    
    print(numbers)
    equation = do_the_magic_for_me(values, answer)
    print(equation, '=', answer)
    
    equation = equation+"\n"
    
    s.send(equation.encode())
    print(s.recv(1024).decode("utf-8"))
    
#  0 1 2
#  ( )      0 1
#    ( )    1 2

# 3 -> 2

#  0 1 2 3
#  ( )       0 1
#    ( )     1 2
#      ( )   2 3
# (( ) )     0 1 0 2
#   (( ) )   1 2 1 3
#    ( ( ))  1 3 2 1
# (  ( ))    0 2 1 2
