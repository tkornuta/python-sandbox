# https://leetcode.com/problems/add-two-numbers/

def addTwoNumbers(l1: list , l2: list ) -> list:
    # Make both list of the same length.
    result = []
    
    # Case I: l1 longer.
    while len(l1) > len(l2):
        l2.append(0)
    
    # Case II: l2 longer.
    while len(l2) > len(l1):
        l1.append(0)
    
    # Now both have the same length - start summation.
    for v1, v2 in zip(l1, l2):
        result.append(v1+v2)
    
    # Finally, deal with values > 10.
    last = 0
    for i in range(len(result)):
        if last > 0:
            result[i] += last
            last = 0

        while result[i] >= 10:
            result[i] -= 10
            last += 1
    # We may have to add a new digit.
    if last > 0:
            result.append(last)

    # Return.
    return result #[::-1]


#l1 = [2,4,3]
#l2 = [5,6,4]
# 342 + 465 = 807

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
# 9999999 + 9999 = 10009998

#l2 = [1, 2, 3]
#l1 = [1, 9]
# 321 + 91 = 412

#l1 = []
#l2 = [1, 2, 3]

print(addTwoNumbers(l1, l2))