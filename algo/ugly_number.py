# https://www.programcreek.com/2014/05/leetcode-ugly-number-java/
# factors only include 2, 3, 5. 
# For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7

# 0 ?
# 1 u
# 5 u 5
# 6 u 2, 3
# 7 n 7
# 8 u 2, 2, 2
# 9 u 9, 9
# 10 u 2, 5
# 11 n 11
# 12 u 2, 2, 3
# 13 u 13
# 14 n 2, 7
# 15 u 3, 5
# 16 u 2, 2, 2, 2
# 17 n
# 18 u 

def is_ugly(num):
    if (num == 1):
        # Break recursion.
        return True
    elif (num == 0):
        return False
    elif (num % 2 == 0):
        return is_ugly(num/2)
    elif  (num % 3 == 0):
        return is_ugly(num/3)
    elif  (num % 5 == 0):
        return is_ugly(num/5)
    else:
        # Break recursion 2.
        return False

def is_ugly2(num,  primes = [2, 3, 5]):
    if (num == 1):
        # Break recursion.
        return True
    elif (num == 0):
        return False
    
    for prime in primes:
        if (num % prime == 0):
            return is_ugly2(num/prime,  primes)

    # Break recursion 2.
    return False

if __name__ == "__main__":
    print(is_ugly2(605, primes=[2, 3, 5, 7, 11]))

