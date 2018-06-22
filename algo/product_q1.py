# Problem: large array of numbers. 
# input = [3,5,8,12]
# output = [product of all but input[0], product of all but input[1], 3 * 5 * 12]
# output = [5 * 8 * 12, 3 * 8 * 12, ...]


from functools import reduce
input = [3,5,8,12]
# Baseline
product = reduce((lambda x,y: x*y), input)
print(product)


from functools import reduce
input = [3,5,8,12]
# 1st version
output = []
# Iterate and create lists excluding the given the index.
for i in range(len(input)):
    input_copy = input.copy()
    # Exclude the first element in the list
    input_copy.pop(i)
    # Calculate the product
    output.append(reduce((lambda x,y: x*y), input_copy))
print(output)


#input = [3,5,8,12]
#print([input[1:] if i == 0 else input[:-1] if i == len(input)-1 else input[:i]+input[i+1:] for i in range(len(input))])

from functools import reduce
input = [3,5,8,12]
# 2nd version
#output = [reduce((lambda x,y: x*y), input[:i-1]+input[i+1:]) for i in range(len(input))]
output = [reduce((lambda x,y: x*y), input[1:] if i == 0 else input[:-1] if i == len(input)-1 else input[:i]+input[i+1:]) for i in range(len(input))]
print(output)
# overall complexity: O(n^2)

######################################
    
from functools import reduce
input = [3,5,8,12]
input = [3,5,8, 12]
print(input)
# 4rd version: O(n)
# Edge case II: [0, 1, 0]
input_without_zeros = list(filter(lambda x: x != 0, input))
product = reduce((lambda x,y: x*y), input)
product_without_zeros = reduce((lambda x,y: x*y), input_without_zeros)

num_of_zeros = len(list(filter(lambda x: x == 0, input)))

output = []
for i in range(len(input)):
    if (num_of_zeros == 0):
          output.append(int(product_without_zeros/input[i]))        
    elif (num_of_zeros == 1):
        if (input[i] == 0): 
            output.append(product_without_zeros)
        else: # no zeros in the list EXCLUDING zero
          output.append(0)
    else: # > 1 zeros
        output.append(0)
print(output)
    

#######################################

from functools import reduce
input = [3,5,8,12]
input = [0,3,5,8,0,12]
# 3rd version: O(n)
# Edge case II: [0, 1, 0]
input_without_zeros = list(filter(lambda x: x != 0, input))
product_without_zeros = reduce((lambda x,y: x*y), input_without_zeros)

num_of_zeros = len(list(filter(lambda x: x == 0, input)))
print(input.index(0))

output = []
for i in range(len(input)):
    if (input[i] == 0):
        output.append(product_without_zeros)
    else: # no zeros in the list EXCLUDING zero
        output.append(product_without_zeros/input[i])
print(output)
    

######################################
    
from functools import reduce
input = [3,5,8,12]
print(input)
# 5th version: O(n)
num_of_zeros = len(list(filter(lambda x: x == 0, input)))

if (num_of_zeros == 0):
    product = reduce((lambda x,y: x*y), input)
    output = [int(product/input[i]) for i in range(len(input))]
elif (num_of_zeros == 1):
    input_without_zeros = list(filter(lambda x: x != 0, input))
    product_without_zeros = reduce((lambda x,y: x*y), input_without_zeros)
    output = [int(product_without_zeros) if input[i] == 0 else 0 for i in range(len(input))]
else: # num zeros > 1
    output = [0] * len(input)        
print(output)

