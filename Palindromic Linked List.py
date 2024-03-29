# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         nums = []
        
#         while head:
#             nums.append(head.val)
#             head = head.next
            
#         l, r = 0, len(nums)-1
        
#         while l <= r:
#             if nums[l] != nums[r]:
#                 return False
            
#             l += 1
#             r -= 1
            
#         return True
    
    
    
        fast = head
        slow = head
        
        #find middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        #reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        #check if palindrome
        
        l , r = head , prev
        
        while r:   #means right=prev not Null, its not in the middle
            if r.val != l.val:
                return False
            
            r = r.next
            l = l.next
            
            
        return True
            