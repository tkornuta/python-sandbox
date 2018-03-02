# https://www.programcreek.com/2014/05/leetcode-ugly-number-ii-java/

# 2, 3, 5
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# 1 u
# 2 u 2
# 3 u 3
# 4 u 2,2
# 5 u 5
# 6 u 2, 3
# 8 u 2, 2, 2
# 9 u 3,3
# 10 u 2, 5
# 12 u 2, 2, 3
# 15 u 3,5
# 16 u 2 2 2 2
# 18 u 2 3 3
# 20 u 2 2 5
# 24 u 2 2 2 3
# 25 u 5 5
    
def nthUglyNumber(n):
    if(n<=0):
        return 0
 
    list_vals = [1]
 
    # Indices for tracking which unumber should be multiplied by a given factor got get the next candidates
    i=0
    j=0
    k=0
 
    while(len(list_vals)<n):
        print("i={}, j={}, k={}".format(i, j, k))
        print("v(i)={}, v(j)={}, v(k)={}".format(list_vals[i],  list_vals[j],  list_vals[k]))
        m2 = list_vals[i] * 2
        m3 = list_vals[j] * 3
        m5 = list_vals[k] * 5
        print(m2,  m3,  m5)
 
        min_val = min(m2, m3, m5)
        list_vals.append(min_val)
        print("After append: ", list_vals)
 
        # As min can result from several combinations - we should increment all of them.
        if(min_val==m2):
            i = i+1
            print("incrementing index 0 (2)")
 
        if(min_val==m3):
            j = j+1
            print("incrementing index 1 (3)")
 
        if(min_val==m5):
            k = k+1
            print("incrementing index 2 (5)")
 
    return list_vals[-1]
    
    
    
def nthSuperUglyNumber(nth,  factors = [2, 3, 5]):
    # Edge cases I & II
    if nth == 0:
        return 0
    elif nth == 1:
        return 1
    
    unums =[1]
    # Addresses pointing which unms should be considered as next candidates.
    # Each adddress is associated with one factor.
    addresses = [0] * len(factors)
    
    # Perform nth-1 times (as we got 1st unum already).
    for _ in range(nth-1):
        # Calculate list of candidates.
        ucands = [unums[addresses[i]]*factors[i] for i in range(len(factors))]
        # Find the minimum ugly number.
        min_ucand = min(ucands)
        unums.append(min_ucand)
        # Increment adrresses that might be used for calculation of a given unumber.
        addresses = [addresses[i]+ 1 if min_ucand == ucands[i] else addresses[i] for i in range(len(factors))]

        print("unums=",unums)
    
    return unums[-1]
    

if __name__ == "__main__":
    print(nthSuperUglyNumber(20))
