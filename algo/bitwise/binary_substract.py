# https://www.geeksforgeeks.org/subtract-two-numbers-without-using-arithmetic-operators/


def subtract(x, y): 
    print("x : {0:b}".format(x))
    print("y : {0:b}".format(y))

    # Iterate till there 
    # is no carry 
    while (y != 0): 
        print("~x: {0:b}".format(~x))
        print("y : {0:b}".format(y))
      
        # borrow contains common  
        # set bits of y and unset 
        # bits of x 
        borrow = (~x) & y 
        print("b : {0:b}".format(borrow))
          
        # Subtraction of bits of x 
        # and y where at least one 
        # of the bits is not set 
        x = x ^ y 
        print("x : {0:b}".format(x))
  
        # Borrow is shifted by one  
        # so that subtracting it from  
        # x gives the required sum 
        y = borrow << 1
        print("last y : {0:b}".format(y))
      
    return x 
  
  
# Driver Code 
x = 2
y = 1
print("x - y is",subtract(x, y)) 

