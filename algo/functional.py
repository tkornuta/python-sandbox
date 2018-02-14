from functools import reduce

# Reduce
list1 = [1, 2, 3,  5,  100] 
result1 = reduce((lambda x, y: x+y), list1)
print(result1)

list2 = [3, 2, 4]
result2 = reduce((lambda x, y: x * y), list2)
print(result2)

# Filter
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(list(filter(lambda x: x in a, b)))

print ([x for x in a if x in b])

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Map
x = [1,2,3]
y = [14,51,6]
z = [4,5,16]

print (list(map(lambda x, y, z: x + y+z,  x, y, z)))

print (list(zip(x, y, z)))

