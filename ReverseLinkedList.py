# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## ITERATIVE
#Time complexity = O(n)   , Space Complexity = O(1)
 #if temp = head
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #itertive solution
        prev = None
   
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
            
        return prev


 # if temp  = head.next
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
        

## RECURSION
#Time complexity = O(n)   , Space Complexity = O(n)

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        return self.reverse(head)

    def reverse(self, node, prev=None):

    # if the node if empty return None which is prev
        if not node:     
            return prev

        temp = node.next       # n is set to be the next node of head
        node.next = prev       # 
        
          
        return self.reverse(temp, node)
