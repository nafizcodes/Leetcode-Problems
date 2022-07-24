# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  #empty node - to avoid edge case of inserting into dummy list
        tail = dummy   
        
        while l1 and l2:       # l1 and l2 are not null
            if l1.val < l2.val:
                tail.next = l1  # if l1 value is less then, add l1 to the output or else otherwise
                l1 = l1.next
                
            else:
                tail.next = l2
                l2 = l2.next
                
            tail = tail.next   # update the tail to the tail.next which moves the pointer to move forward
        
        # runs out of any one of the list items
        
        if l1:         #if l1 is empty   
            tail.next = l1    #add the remaining of l1 to the output
        elif l2:       #likewise
            tail.next = l2
            
        return dummy.next      #returns the head of the output 
                
                
            