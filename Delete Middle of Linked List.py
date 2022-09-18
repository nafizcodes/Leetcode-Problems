# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head.next:  #handling the edge case of 1 node
#             return head.next
        
#         slow , fast = head, head.next.next
        
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
            
#         slow.next = slow.next.next
        
#         return head
        
        dummy = ListNode(None,head)   #to avoid the edge case of 1 node, deleting 1node gives empty list
        slow, fast = dummy, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = slow.next.next
        
        return dummy.next
            