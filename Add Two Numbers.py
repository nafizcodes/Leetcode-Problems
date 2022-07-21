# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0 
        
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            #new digit
            sum_val = val1 + val2 + carry 
            
            carry = sum_val // 10   #carry is the floor division - quotient
            rem = sum_val % 10   #remainder is the modulus 
            
            curr.next = ListNode(rem)
            
            curr = curr.next
            
            #update ptrs
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            
        return dummy.next
            
#Time Complexity - O(n)  iterating through listnodes n+n O(2n)
#Space - O(1) 