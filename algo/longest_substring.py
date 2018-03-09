#https://www.programcreek.com/2013/02/longest-substring-which-contains-2-unique-characters/

def longest_substring_hashmap(str,  k):
    print("Input = ",  str)
    if len(str) < 2:
        return []
    
    # Best (longest) substring.
    best_first_index = 0
    best_last_index = 0
    best_len = 0

    # Set pointer to first element of substring.
    first_index = 0
    last_index = 1
    # Hashmap counting how many times given element was seen.
    ucmap = {str[0]: 1}
    print(ucmap)
    
    # Iterate through elements. 
    for i in range(1, len(str)):
        print(i,  str[i])
        if (str[i] in ucmap):
            ucmap[str[i]] = ucmap[str[i]] +1
        else:
            ucmap[str[i]] = 1
        print(ucmap)
        print("fi = {}, li = {}".format(first_index,  last_index))      
        # Check number of element in hashmap.
        if (len(ucmap) <= k):
            # Perfect, the substring is "growing".
            last_index = i
        else:
            print("oo")
            # Oo, to many different symbols.
            tmp_len = last_index - first_index +1
            print("tmp_len =",  tmp_len)
             # if it is the best subsequence - remember it.
            if (best_len < tmp_len):
                best_first_index = first_index 
                best_last_index = last_index
                best_len = tmp_len
                print("best fi = {}, li = {}".format(best_first_index,  best_last_index))      
            # And proceed - pop from hashmap the symbols that apear on the left
            while  (len(ucmap) > k):
                print("while decrement")
                # Get symbol.
                char = str[first_index]
                if ucmap[char] == 1:
                    ucmap.pop(char, None)
                else:
                # Decrement
                    ucmap[char] = ucmap[char]  - 1
                # Move index to left
                first_index = first_index +1
            print("ucmap after decrement:", ucmap)
            print("first_index=", first_index)
                
    # The string ended. Check the last substring.
    tmp_len = last_index - first_index +1 # As we cound the last_index IN this time!
    print("tmp_len =",  tmp_len)
     # if it is the best subsequence - remember it.
    if (best_len < tmp_len):
        best_first_index = first_index 
        best_last_index = last_index+1 # As we cound the last_index IN this time!
        best_len = tmp_len
        print("best fi = {}, li = {}".format(best_first_index,  best_last_index))  
        
    print("final fi = {}, li = {}".format(best_first_index,  best_last_index))      
    return str[best_first_index:best_last_index]





def longest_substring(str,  k):
    ''' Simple solution with O(n^2) time complexity.'''
    if len(str) < 2:
        return []

    # Best (longest) substring.
    best_first_index = 0
    best_last_index = 0
    best_len = 0

    # Iterate through elements.
    for i in range(len(str)):
        # Add first char to list of unique chars.
        unique_chars = [str[i]]
        # Set pointer to first element of substring.
        first_index = i
        # And assume that the substring will contain all the following elements.
        last_index = -1
        for j in range(i+1, len(str)):
            if str[j] in unique_chars:
                # If the character is in list - move last index.
                last_index = j
                continue
            elif len(unique_chars) <k:
                # Else: if this is second character.
                unique_chars.append(str[j])
                # Move last index.
                last_index = j
                continue
            else:
                # This is third character - the substring ended at j-1.
                break
        print("i = {}, j = {}, fi = {}, li = {}".format(i,  j,  first_index,  last_index))
        # Check whether this is the longest substring found yet.
        if (last_index > 0 ):
            print("elo")
            length = last_index - first_index
            # if it is - remember it.
            if (best_len < length):
                best_first_index = first_index 
                best_last_index = last_index
                best_len = length
            print("best fi = {}, li = {}".format(best_first_index,  best_last_index))
    
    # Edge case III: there is no subsequence that consists of 2 elements.
    if (best_len == 0):
        return []
    # Return the best subsequence
    return str[best_first_index:best_last_index]
    
if __name__ == "__main__":
    # Edge case I: no symbols
    str = ""
    # Edge case II: single symbol 
    str = "aaaaaab"
    
    str = "abcbbbbcccbdddadacb"
    #str = "abbcadcacacaca"
    print("longest =", longest_substring_hashmap(str, 2))
