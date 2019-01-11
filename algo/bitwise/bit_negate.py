# Negate int with bitwise operations only.

def bit_negate(d):
    print("bit     d: {0:b}".format(d))

    negation = 1
    for _ in range(d.bit_length()-1):
        negation = negation << 1 | 1
    print("negation: {0:b}".format(negation))

    neg_d =  ~d 
    neg_d = (neg_d^1)|((neg_d&1)<<1)

    print("bit neg_d: {0:b}".format(neg_d))
    return neg_d

# printf("%d",(i^j)|((i&j)<<1));

if __name__ == "__main__":
    d = 10
    print(bit_negate(d))
