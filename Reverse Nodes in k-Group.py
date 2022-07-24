# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy #to save the node of one node prior to the kth node
        #for instance
        #1 -> 2 -> 3  if we were to reverse 2->3, we need pointer to one node before kth 
        #1 -> 3 -> 2  
        
        while True:
            kth = self.getKth(groupPrev, k)  #gives the kth value (dummy->1->2 here k will be 2)
            if not kth:  #cases like 1->2->3 where the k will be Null
                break
            
            groupNext = kth.next  # node after the kth node, here 3 initially
            
            #reverse group
            #prev is not equal to null as it will split the list
            
            #here prev = 3  for 1->2->3  curr = 1
            prev, curr = kth.next, groupPrev.next   
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr 
                curr = tmp
            
            tmp = groupPrev.next   # 1     
            groupPrev.next = kth   # 2   dummy -> 2 -> 1 
            groupPrev = tmp        # groupPrev = 1
            
        return dummy.next
            
    def getKth(self, curr, k):  #curr = dummy, k = 2
        while curr and k > 0 :  
            curr = curr.next    #1st pass: curr = 1, k=1 ; 2nd pass: curr = 2, k = 0
            k-=1
        return curr     #curr = 2
    
    