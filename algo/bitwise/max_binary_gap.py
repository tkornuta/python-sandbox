# Problem: Get maximum binary Gap.
# For example, 9's binary form is 1001, the gap is 2. 
# https://www.programcreek.com/2013/02/twitter-codility-problem-max-binary-gap/

def max_binary_gap(bits):
    print(value)
    # change to digit.
    d = int(bits, 2)

    max_gap = 0 
    current_gap = 0

    while (d>0):
        print("{0:b}".format(d))
        # Check last bit.
        if d & 1 == 0:
            current_gap += 1
            max_gap = max(max_gap, current_gap)
            print("gap = ", current_gap)
        else:
            current_gap = 0
        # Shift right by one bit.
        d = d >> 1
    
    return max_gap


if __name__ == "__main__":
    value = "1000111001"
    print(max_binary_gap(value))