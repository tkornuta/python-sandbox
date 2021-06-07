# https://www.programcreek.com/2012/12/leetcode-3sum/
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
from typing import List

arr1 = [-1, 0, 1, 2, -1, -4]

def find_3sum_brute(arr: List[int]):
    # Edge case: less than 3 elements.
    if len(arr) < 3:
        return False
    narr = len(arr)
    # Array of triplets.
    triplets = []
    triplet_strs = []
    # Brute force loop: O(n^3) 
    for i in range(narr):
        for j in range(i+1, narr):
            for k in range(j+1, narr):
                # 
                if arr[i]+arr[j]+arr[k] == 0:
                    # Ok, we got the triplet - make it non-descending.
                    triplet = [arr[i], arr[j], arr[k]]
                    triplet.sort()
                    # Make unique "string hash".
                    triplet_str = '.'.join([str(i) for i in triplet])
                    # Check if given triplet was already found.
                    if triplet_str not in triplet_strs:
                        # Ok, got a new one! :)
                        triplets.append(triplet)
                        triplet_strs.append(triplet_str)
    # Return the list of found triplets.
    return triplets



def find_3sum_sort(arr: List[int]):
    # Edge case: less than 3 elements.
    if len(arr) < 3:
        return False
    narr = len(arr)
    arr.sort()
    print(arr)
    # Array of triplets.
    triplets = []
    triplet_strs = []

    #for i in range(narr):
    #    # Take min and max.
    #    j = 


    # Return the list of found triplets.
    return triplets


print(find_3sum_sort(arr1))
