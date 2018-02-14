
def rev(str):
    list = str.split()
    reversed_str = ""
    # Remove in reversed order.
    while len(list) > 0:
            w = list.pop()
            for l in range(len(w)-1, -1,  -1) :
                reversed_str = reversed_str + w[l]
            reversed_str = reversed_str  + " "
    # Print the result.
    print (reversed_str)

def rev2(str):
    print (str[::-1])
    
if __name__ == "__main__":
    rev("Hello World")
    rev("Geeks for Geeks")
    


