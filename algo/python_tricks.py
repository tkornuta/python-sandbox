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
