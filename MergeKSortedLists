# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            combinedList = []
            for i in range(0, len(lists), 2):
                
                l1 = lists[i]
                # if the length is even then l2 = list[i+1]
                #else: odd, then return None meaning, in the next loop l1 will be remaining one list
#                 if (i+1) < len(lists):
#                     l2 = lists[i+1]
#                 else:
#                     None
                    
                l2 = lists[i+1] if (i+1) < len(lists) else None
                combinedList.append(self.merge(l1,l2))
            
            lists = combinedList
            
        return lists[0]
            
    def merge(self, l1, l2):
        dummy = ListNode()
        output = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                output.next = l1
                l1 = l1.next
            else:
                output.next = l2
                l2 = l2.next
            output = output.next
                
        if l1:
            output.next = l1
        elif l2:
            output.next = l2
        
        return dummy.next