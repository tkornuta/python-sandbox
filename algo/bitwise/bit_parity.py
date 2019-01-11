# https://wiki.python.org/moin/BitManipulation
# From "Bit Twiddling Hacks" 
# returning 0 if there are an even number of set bits, and -1 if there are an odd number.

def bit_parity(d):
    print("{0:b}".format(d))

    parity = 0

    while (d):
        parity = parity ^ (d & 1)
        d = d >> 1

    return parity


def parityOf(int_type):
    print("{0:b}".format(d))
    parity = 0
    while (int_type):
        parity = ~parity
        int_type = int_type & (int_type - 1)
    return parity


if __name__ == "__main__":
    d = 7
    print(parityOf(d))
    #print(bit_parity(d))