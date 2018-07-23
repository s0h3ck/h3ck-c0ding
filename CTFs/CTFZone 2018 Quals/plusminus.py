from itertools import product
from itertools import combinations

operators = ['+', '*', '-', '/']
values = ['1', '2', '3', '1']
answer = '6'

length_values = len(values)
number_of_space = length_values - 1

possible_pairs = []

for pair in combinations([i for i in range(0, length_values)], 2):
    possible_pairs.append(list(pair))

for layer in range(0, length_values-1):
    for pair in combinations(possible_pairs, layer+1):
        list_of_pairs = list(pair)

        tmp_values = values[:]
        
        for position_pair in list_of_pairs:
            tmp_values[position_pair[0]] = '(' + tmp_values[position_pair[0]]
            tmp_values[position_pair[1]] = tmp_values[position_pair[1]] + ')'

        current_layer = ' '.join(tmp_values)
        
        for i in product(operators, repeat=number_of_space):
            equation = current_layer

            for j in range(0, number_of_space):
                equation = equation.replace(' ', i[j], 1)

            try:
                r = eval(equation)

                if str(r) == answer:
                    print(equation, '=', r)
            except:
                pass
