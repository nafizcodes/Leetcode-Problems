# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next   # two pointers to split the list into two, slow for the first half, fast for the second half
        
        while fast and fast.next:  #fast is not null (odd) and fast.next is not null(even)
            slow = slow.next       #slow moves by one position
            fast = fast.next.next  #fast moves by two
            
        #after traversing the list and arranging the pointers
        second = slow.next  #second is the next node of slow
        slow.next = None    #this is splitting the list
        
        #reversing the second list because or else cannot move back if it is inorder(3-> 4), link gets broken and we cannot move back
        prev = None
        while second:
            temp = second.next 
            second.next = prev  
            prev = second
            second = temp
            
        # or we can do,
        #     temp = second
        #     second = second.next
        #     temp.next = prev
        #     prev = temp
        
        #Merge two halfs
        second = prev   #from the reversed list, prev is the start of second list now
        first = head    #head itself is the head of the first
        
        while second:   #second might be smaller and run out, as seen in the diagram
        #Merging
            temp1 = first.next  
            temp2 = second.next 
            first.next = second
            second.next = temp1
            
        #Shifiting the pointers
            first = temp1
            second = temp2
