def total_xor(a):
    """ Calculates the XOR total run from [0, a] """
    # Special case:
    if (a <= 0):
        return 0
    res = [a,1,a+1,0]
    return res[a%4]
    
def a_to_b_xor(a, b):
    """ Calculates the XOR total run from [a, b], assuming that b > a """
    return total_xor(b)^total_xor(a-1)

def answer(start,  length):
    """ Calculates the security sum"""

    # Edge case 0: 
    if (length == 1):
        return start
    
    # Control sum
    control_sum = 0
    # Value.
    current_val = start
    # Chunk (subsequence) params.
    len = length
    offset = 1
    # Iterate through chunks
    while (len > 1):
        # Get chunk first and last values.
        first = current_val
        last = first + len -1
        #print("first = {}, last = {}".format(first,  last))
        # Update control sum.
        control_sum = control_sum ^ a_to_b_xor(first,  last)
        #print("control_sum = {}".format(control_sum))
        # Move to the next chunk.
        current_val = last + offset
        # Update chunk offset and length.
        len = len -1
        offset = offset+1
    # Handle remaining element.
    #print("last val = {}".format(current_val))
    control_sum = control_sum ^ current_val
            
    # Return sum.
    return control_sum


if __name__ == "__main__":
    #print(total_xor(4 ))
    
    #print(2^3^4)
    #print(a_to_b_xor(2, 4))
    
    #print(answer(1,  10)) # 10
    
    print(answer(0,  3)) # 2
    
    print(answer(17,  4)) # 14
    

