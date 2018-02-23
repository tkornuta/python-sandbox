# Problem: large array of numbers. 
# input = [3,5,8,12]
# output = [product of all but input[0], product of all but input[1], 3 * 5 * 12]
# output = [5 * 8 * 12, 3 * 8 * 12, ...]

input = [3,5,8,12]

# Baseline
product = reduce((lambda x,y: x*y), input)

# 1st version
output = []
# Iterate and create lists excluding the given the index.
for i in range range(len(input)):
    input_copy = input.copy()
    # Exclude the element in the list
    input_copy.pop(i)
    # Calculate the product
    output.append(reduce((lambda x,y: x*y), input_copy))

# 2nd version
output = [reduce((lambda x,y: x*y), input.copy().pop(i)) for i in range range(len(input))]
# overall complexity: O(n^2)


# 3rd version: O(n)
# Edge case II: [0, 1, 0]
input_without_zeros = list(filter(lambda x: x != 0, input))
product = reduce((lambda x,y: x*y), input)
product_without_zeros = reduce((lambda x,y: x*y), input_without_zeros)


output = []
for i in range(len(input)):
    if (number of zeros > 1): # more than 1 zero
        output.append(0)
    elif (input[i] == 0): # at most 1 zero in the whole input list
        output.append(product_without_zeros)
    else: # no zeros in the list EXCLUDING zero
        output.append(product_without_zeros/input[i])
    
    

    
