# Reverse bits of a given 32 bits unsigned integer.
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
# return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
# https://www.programcreek.com/2014/03/leetcode-reverse-bits-java/

def reverse_bits(d, bits_to_fill=32):
    print("{0:b}".format(d))
    # Get number of bits.
    n = d.bit_length()

    rev_d = 0
    need_to_shift = 0
    for shift in range(n):
        need_to_shift +=1
        print("{0:b}".format(d >> shift))
        if d & (1 << shift):
            rev_d = rev_d << need_to_shift | 1
            need_to_shift = 0

    # Fill to 32 bits.
    if d.bit_length() < bits_to_fill:
        for _ in range(bits_to_fill-d.bit_length()):
            rev_d = rev_d << 1
    
    print("d    : {0:b}".format(d))
    print("Rev d: {0:b}".format(rev_d))    
    return rev_d


if __name__ == "__main__":
    d = 43261596
    print(reverse_bits(d,-1))