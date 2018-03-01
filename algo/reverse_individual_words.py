# https://www.programcreek.com/2014/05/leetcode-reverse-words-in-a-string-ii-java/

#Given s = "the sky is blue",
#return "blue is sky the".

import math

def reverse_array(arr,  fi,  li):
    """ Reverses array from position fi to li
    O(1) space and O(n) operations -> n/2 * 2 swaps.
    """
    for i in range(math.ceil((li-fi)/2)):
        # Calculate "mirrored" indices
        ii = fi + i
        jj = li - i
        #print("ii={}, jj={}".format(ii, jj))
        # Swap.
        tmp = arr[ii]
        arr[ii] = arr[jj]
        arr[jj] = tmp

def rev(str):
    print(str)
    arr = list(str)
    print(arr)
    
    # Empty list.
    if (len(arr) <1):
        print("Edge case 0")
        return str

    # Find first space.
    i=0
    if (arr[i] == ' '):
        while (i < len(arr)) and (arr[i] == ' '):
            i = i+1
    # Ok, got the letter.
 
    # Edge case - no words
    if (i >= len(arr)):
        print("Edge case 1")
        return str

    # Go and reverse words, one by one.
    j=i+1
    while(j < len(arr)):
        # Skip letters forming given word.
        while (j < len(arr)) and (arr[j] != ' ') :
            j = j+1

        #print("i={}, j={}".format(i, j))
        # Else: reverse the word
        reverse_array(arr,  i,  j-1)
        
        # And move to the next word.
        i=j+1
        # Skip spaces
        while (i < len(arr)) and (arr[i] == ' '):
                i = i+1
       # Ok, got letter (or end of the word)
        j = i+1
        
    # At the end: reverse the whole array.
    reverse_array(arr,  0, len(arr)-1)
    
    # We could use list slicing - but it creates new list, we O(1) space won't hold anymore.
    # arr = arr[::-1]
    
    return ''.join(arr)

    
if __name__ == "__main__":
    str = "Hello World"
    str = "the sky is blue" 
    #str = "abcde"
    #str="a    alka    abd "
    print("")
    print(rev(str))
    
    


