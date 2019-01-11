# Get sign with bitwise operations only.

def bit_sign(d):
    print("d: {0:b}".format(d))

    sign = ~d ^ d

    return sign

def sign(x):
    return 1*(x>0)
    #return 1-(x<=0)

if __name__ == "__main__":
    d = -7
    print(bit_sign(d))
