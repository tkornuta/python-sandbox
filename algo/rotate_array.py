# https://www.programcreek.com/2015/03/rotate-array-in-java/

import math

def rotate_list(arr,k):
    """ First idea: jump between adrresses by k as many times as num of elements and overwrite values with ones from previous address.
    O(2) space and O(n) time
    """
    # Length of array.
    arl = len(arr)

    # Edge cases I & II: k=0 or empty list
    if arl < 2 or k == 0:
        print("Edge case")
        return arr

    # Previous index and element.
    prev_ind = 0
    prev_val = arr[0]

    # Perform the shift n times.
    for _ in range(arl):
        # Jump to "destination address adrres 
        ind = (prev_ind + k) % arl
        #print(ind)
        # Store variable.
        val = arr[ind]
        # Overrite variable.
        arr[ind] =prev_val
        # "Update"
        prev_ind = ind
        prev_val = val
    
    return arr

def swap_symmetric(arr,  i, first,  arl):
    """ Swaps two array elements lying on the oposite sides of vector of length arl"""
    #print("i+first={}".format(i+first))
    tmp = arr[i+first]
    #print("first + ((arl-1-i) % arl)={}".format(first + ((arl-1-i) % arl)))
    j = first + ((arl-1-i) % arl)
    arr[i+first] = arr[j]
    arr[j] = tmp
    
def rotate_list2(arr,k):
    """ Found idea: Use three reverses.
    O(1) space and O(2*n) time => o(n)
    """
    # Length of array.
    arl = len(arr)
    
    # Edge cases I & II: k=0 or empty list
    if arl < 2 or k == 0:
        print("Edge case")
        return arr
    
    # Modulo the shift.
    if (k>arl)or (k<0):
        k = k % arl

    # Reverse the whole list - swap.
    for i in range(math.floor(arl/2)):
        swap_symmetric(arr,  i,  0,  arl)
        
    #print("reswap1")
    # Re-swap first k elements
    for i in range(math.floor(k/2)):
        swap_symmetric(arr,  i,  0,  k)
        
    #print("reswap2")
    # Re-swap the rest of elements
    for i in range(math.floor((arl - k)/2)):
        swap_symmetric(arr,  i,  k, arl-k)

    # Return the array.
    return arr
    
    
 
if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    #arr = [1, 2, 3]
    print(rotate_list2(arr, -2))
