# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow , fast = head, head
        
        #fast = head.next wont work , fails one testcase: [] pos = -1 , empty node doesnt have a next pointer 
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            
            if slow == fast:
                return True
            
        return False