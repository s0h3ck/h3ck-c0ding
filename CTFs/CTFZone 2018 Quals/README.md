# CTFZone 2018 Quals writeup

## PlusMinus
**Category:** PPC
**Points:** 101
**Solves:** 
**Description:**

> To solve this task, you need to put arithmetic operators into expression in the right order. Allowed operators: + - / * (). Final expression must involve all the supplied numbers and the number order must be the same as in original expression. The last number in the line should be an answer.

## Write-up
The idea behind this problem is to try to find all the equations to match an answer. Once we have an equation, we send it to the machine. 

Just to be ready, let's make an example. Let's consider the sequence `['1', '2', '3', '6']`. The last number, `6` is the answer we want. The first three numbers are the "tools" to get to it.

Having said that, all the possible equations are :

```text
(1+2)+3 = 6
(1*2)*3 = 6
(1+2+3) = 6
(1*2*3) = 6
1+(2+3) = 6
1*(2*3) = 6
((1+2)+3) = 6
((1*2)*3) = 6
(1+(2)+3) = 6
(1*(2)*3) = 6
(1+(2+3)) = 6
(1*(2*3)) = 6
```

Cool, huh!?
Ok, magician... Can you show us the script?

Here is my reflexion. The values cannot move and must remain in the same order. So, we do not touch them.

Once you put the numbers next to each other, imagine you have a white square or rectangle. Remembering your first homework when you were young? ;)

Well, in our case, shapes will be spaces. We will understand it more later when we will solve it.

We will get something like:

```python
operators = ['+', '*', '-', '/']
values = ['1', '2', '3']
answer = '6'

length_values = len(values)
number_of_space = length_values - 1
```

Then, we have to add the parentheses. We compute all possible pairs of parentheses.

For instance, for three values, we can only compute a minimum of two pairs of parentheses.
```text
1 2 3
( ) 
  ( )
```

We will come up with the following code.

```python
possible_pairs = []

for pair in combinations([i for i in range(0, length_values)], 2):
    possible_pairs.append(list(pair))
```

Then, we will need to compute different layers of parentheses if we have more than three values.

Again, an example:
```text
 0 1 2 3
 ( )       0 1
   ( )     1 2
     ( )   2 3
(( ) )     0 1 0 2
  (( ) )   1 2 1 3
   ( ( ))  1 3 2 1
(  ( ))    0 2 1 2
```

So, we come up with something like that:
```python
for layer in range(0, length_values-1):
    for pair in combinations(possible_pairs, layer+1):
        list_of_pairs = list(pair)
```

Then, we add the parentheses, left and right.

```python
tmp_values = values[:]

for position_pair in list_of_pairs:
    tmp_values[position_pair[0]] = '(' + tmp_values[position_pair[0]]
    tmp_values[position_pair[1]] = tmp_values[position_pair[1]] + ')'

    current_layer = ' '.join(tmp_values)
```

Next, we fill the spaces by swapping the operators in the equation, we evalute the equation and compare to the answer. If it matches, we send it to our machine. If not, the computer will do the rest for me ;)

Our last piece of code.
```python
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
```

The code all together.

```python
from itertools import product
from itertools import combinations

operators = ['+', '*', '-', '/']
values = ['1', '2', '3']
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
```

Finally, we add the code designed above to solve the challenge. Here is the code used for the CTF.

The flag is `=> ctfzone{DCF58FFDDA7CE9F0EA0D93C0E030FC06}`

## Notes
- The solution is not perfect. For example, if you look carefully the first demonstration, the script computes outside parentheses before inside parentheses. This is a waste of energy.

```
(1*2*3) = 6
1+(2+3) = 6
```

- Probably, thinking in term of trees and tuples ;)

If you have any comments, reach me out, I would love to hear from you :)
