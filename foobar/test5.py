def answer(start,  length):
    """ Calculates the security sum"""

    # Edge case 0: 
    if (length == 1):
        return start
    
    # Take first id.
    cur_id = start
    control_sum = 0

    for i in range(length,  0,  -1):
        for j in range(length):
            if j < i:
                # Get id.
                control_sum = control_sum ^ cur_id
                print ("i= {}, j = {}, cur_id = {}({}), control_sum = {}({})".format(i, j, cur_id,  bin(cur_id),  control_sum,  bin(control_sum)))
            # Increment id.
            cur_id = cur_id +1
            
    # Return sum
    return control_sum


if __name__ == "__main__":

    #print(answer(1,  10)) # 10
    
    #print(answer(0,  5)) # 2
    
    print(answer(17,  4)) # 14
    

