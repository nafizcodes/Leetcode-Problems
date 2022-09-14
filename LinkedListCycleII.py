class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                pointer = head 
                while pointer != fast:
                    pointer = pointer.next
                    fast = fast.next
            
                return pointer
                
        return None