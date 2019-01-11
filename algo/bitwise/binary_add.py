# https://www.programcreek.com/2014/05/leetcode-add-binary-java/
# Given two binary strings, return their sum (also a binary string).
# For example, a = "11", b = "1", the return is "100".

def binary_add(d1, d2):
    s1 = "{0:b}".format(d1)
    s2 = "{0:b}".format(d2)
    print("s1     = ",s1)
    print("s2     = ",s2)

    result =''
    carry = False

    # Make both strings equal when it comes to lengths
    n = max(len(s1),len(s2))
    ext_s1 = s1.rjust(n, '0')
    ext_s2 = s2.rjust(n, '0')
    print("ext_s1 = ",ext_s1)
    print("ext_s2 = ",ext_s2)

    for b1,b2 in zip(reversed(ext_s1),reversed(ext_s2)):
        ones = carry == True
        if b1 == "1":
            ones += 1 
        if b2 == "1":
            ones += 1 
        # Check number of ones.
        if ones == 0:
            result = "0" + result
            carry = False
        elif ones == 1:
            result = "1" + result
            carry = False
        elif ones == 2:
            result = "0" + result
            carry = True
        else:
            result = "1" + result
            carry = True
    # Handle last carry.
    if carry:
        result = "1" + result
    print("Result = ",result)

    return int(result, 2)


def binary_add2(d1,d2):
    print("d1: {0:b}".format(d1))
    print("d2: {0:b}".format(d2))

    while d2:
        a = (d1^d2)
        b = (d1&d2) << 1
        print("a : {0:b}".format(a))
        print("b : {0:b}".format(b))
        d1 = a | b 
        d2 =  a & b
        print("d1: {0:b}".format(d1))
        print("d2: {0:b}".format(d2))
        
    print("r:  {0:b}".format(d1))
    return d1

if __name__ == "__main__":
    d1 = 5
    d2 = 5
    print(binary_add2(d1,d2))

