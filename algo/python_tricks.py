# https://docs.python.org/2/howto/functional.html

import itertools

A = list(zip([1,3,5,7,9],[2,4,6,8,10]))
B = [1,3,5,7,9]+[2,4,6,8,10]
C = list(set([1,3,5,7,9] + [2,4,6,8,10]))

D = [1,3,5,7,9]
D.append([2,4,6,8,10])

E = [1,3,5,7,9]
E.extend([2,4,6,8,10])

F = []
for a in itertools.chain([1,3,5,7,9], [2,4,6,8,10]):
    F.append(a)


print ("A: " + str(A))
print ("B: " + str(B))
print ("C: " + str(C))
print ("D: " + str(D))
print ("E: " + str(E))
print ("F: " + str(F))

#S = set(((2, 2), (3, 5), 5, 7, 11, 13))
#for i in S:
#    print (i)

# MAP
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# FILTER
number_list = range(-5, 5)
print(number_list)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# REDUCE
product = 1
my_list = list(range(1, 5))
for num in my_list:
    product = product * num
print(product)

from functools import reduce
product = reduce((lambda x, y: x * y), my_list)
print(product)
