"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None}
        curr = head
        
        #1st loop : to map the original nodes in a hashmap
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy  #mapping the copy against the curr (old:copy)
            curr = curr.next
            
        curr = head   #reseting the current to head
        #2nd loop to add the pointers to the copied nodes
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]   #edge case - what if the curr.next is null so we do : oldToCopy = {None : None}
            copy.random = oldToCopy[curr.random]
            
            curr = curr.next
            
        return oldToCopy[head]
    
#Time - O(n)  - iterating through the list of nodes
#Space - O(n) - using hashmap of n nodes