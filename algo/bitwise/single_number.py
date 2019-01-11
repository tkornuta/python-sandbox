# Given an array of integers, every element appears twice except for one. Find that single one.
#
# The key to solve this problem is bit manipulation. XOR will return 1 only on two different bits. 
# So if two numbers are the same, XOR will return 0. Finally only one number left.
# https://www.programcreek.com/2012/12/leetcode-solution-of-single-number-in-java/

def single_number(d_list):
    value = 0

    # All the doubling bits will cancel each other.
    for d in d_list:
        value = value ^ d

    return value 


if __name__ == "__main__":
    d_list = [2, 502, 6, 502, 6, 502, 2]
    print(single_number(d_list))