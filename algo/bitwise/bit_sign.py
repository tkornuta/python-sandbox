# Get sign with bitwise operations only.

def bit_sign(d):
    print("d: {0:b}".format(d))

    # NOT WORKING FOR 2,4,8, 16 etc.!!!!
    sign = ((d & (1 << (d.bit_length() - 1))) != 0)

    return sign

def sign(x):
    return 1*(x>0)
    #return 1-(x<=0)

if __name__ == "__main__":
    d = -15
    print(bit_sign(d))
