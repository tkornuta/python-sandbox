# Python 3 program to check if a number can 
# be expressed as sum of consecutive numbers 
  
  
# This function returns true if n  
# can be expressed sum of consecutive. 
def canBeSumofConsec(n) : 
  
    # We basically return true if n is a NOT a power of two!
    return ((n&(n-1)) & n) 
  
  
# Driver code 
n = 8
if(canBeSumofConsec(n)) : 
    print("true") 
else : 
    print("false") 