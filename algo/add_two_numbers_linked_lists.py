# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __len__(self):
        length = 0
        ptr = self
        while (ptr is not None):
            length +=1
            ptr = ptr.next
        return length

    def append(self, val=0):
        cur_ptr = self
        while (cur_ptr.next is not None):
            cur_ptr = cur_ptr.next
        # Add new node.
        cur_ptr.next = ListNode(val=val)

    @staticmethod
    def create(l: Optional[list]=None):
        if l is None or len(l) == 0:
            return ListNode(val=0)
        head = None
        cur_ptr = None
        for val in l:
            # Create head.
            if cur_ptr is None:
                new_ptr = ListNode(val=val)
                head = new_ptr
                cur_ptr = new_ptr
            else:
                new_ptr = ListNode(val=val)
                cur_ptr.next = new_ptr
                cur_ptr = new_ptr
        return head
    
    def __str__(self) -> str:
        cur_ptr = self
        list_descr = "["
        while (cur_ptr is not None):
            list_descr += str(cur_ptr.val) + ","
            cur_ptr = cur_ptr.next
        list_descr = list_descr[:-1] + "]"
        return list_descr
            
        

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge cases: l1 or l2 not present/empty.
        if l1 is None:
            l1 = ListNode.create([0])
        if l2 is None:
            l2 = ListNode.create([0])
        
        # Make both list of the same length.
        result = []
        
        # Case I: l1 longer.
        while len(l1) > len(l2):
            l2.append(val=0)
        
        # Case II: l2 longer.
        while len(l2) > len(l1):
            l1.append(val=0)
        
        # Now both have the same length - start summation
        # Iterate in forward order, add at front -> "reverse iteration".
        while (l1 is not None):
            # Sum elements
            result.append(l1.val+l2.val)
            # Next elements.
            l1 = l1.next
            l2 = l2.next
        
        # Finally, deal with values > 10.
        last = 0
        for i in range(len(result)):
            if last > 0:
                result[i] += last
                last = 0

            while result[i] >= 10:
                result[i] -= 10
                last += 1
        # We may have to add new digit.
        if last > 0:
                result.append(last)
        
        return ListNode.create(result)

#l1 = [2,4,3]
#l2 = [5,6,4]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
#l1 = None
#l2 = [1, 2, 3]
#l1 = [1, 9]
#l2 = []
print(Solution().addTwoNumbers(l1=ListNode.create(l1), l2=ListNode.create(l2)))


# 342 + 465 = 807
# 9999999 + 9999 = 10009998
# 321 + 91 = 412