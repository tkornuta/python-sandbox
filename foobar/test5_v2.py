#import copy

def answer(start,  length):
    """ Calculates the security sum"""

    # Edge case 0: 
    if (length == 1):
        return start
    
    # Reset sum.
    control_sum = 0
    # Id related variables.
    cur_id = start
    
    for i in range(length,  0,  -1):
        j =0
        while j < i:
            # Get id.
            control_sum = control_sum ^ cur_id
            #print ("i= {}, j = {}, cur_id = {}, control_sum = {}".format(i, j, cur_id,  control_sum))
            # Increment id and j.
            cur_id = cur_id +1
            j = j+1
        # At the end: "rewind" the remaining ids.
        cur_id = cur_id + (length - j)
            
    # Return sum
    return control_sum


if __name__ == "__main__":
 
    #print(answer(1,  10)) # 10
    
    #print(answer(0,  3)) # 2
    
    #print(answer(17,  4)) # 14
    
    print(answer(0,  1000)) # ?


