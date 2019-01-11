# Write a function that takes an unsigned integer and returns the number of ’1' bits it has 
# (also known as the Hamming weight).
# https://www.programcreek.com/2014/03/leetcode-number-of-1-bits-java/

def hamming_weight(value):
    bits = "{0:b}".format(value)
    print(bits)
    # Get number of bits.
    l = value.bit_length()
    #print(l)

    # Number of bits that are on.
    on = 0
    for i in range(l):
        #print("{0:b}".format(value >> i))
        if value >> i & 1:
            on += 1

    return on


if __name__ == "__main__":
    value = 124350
    print(hamming_weight(value))