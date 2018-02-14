import numpy as np

def k_largest_elements2(lst,  k):
    """ Get k elements, overwrite biggest elements with small values, uses a separate list"""
    # Edge case.
    if (len(lst) < k):
        k = len(lst)
    # List with values
    largest = []
    # Perform k iterations - so k biggest elemets will appear at the beginning
    for i in range(k):
        max_val = -np.inf
        max_ind = -1
        for i in range(len(lst)):
            if (max_val < lst[i]):
                max_val = lst[i]
                max_ind = i
        # Ok, got the biggest value - store it and override with -inf.
        largest.append(max_val)
        lst[max_ind] = -np.inf
    return largest
    

def k_largest_elements(lst,  k):
    """ Sort the list - partially, using bubblesort and inplace element exchange"""
    # Edge case: length of the list < k 
    if (len(lst) < k):
        # if those elements can be unsorted.
        #return lst
        # Otherwise:
        k = len(lst)
    # Get 3 elements using bubble sort.
    index = len(lst)-1
    sorted_index = 0
    # Perform k iterations - so k biggest elemets will appear at the beginning
    for i in range(k):
        # Perform one iteration of bubblesort.
        for i in range(index,  sorted_index,  -1):
            # Inplace change.
            if (lst[i] > lst[i-1]):
                tmp = lst[i-1]
                lst[i-1] = lst[i]
                lst[i] = tmp
        
    
    return lst[0:k]
    
if __name__ == "__main__":
    lst =  [1, 23, 12, 9, 30, 2, 50] 
    print(k_largest_elements2(lst,  10))
