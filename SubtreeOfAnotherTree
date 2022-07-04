# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not t:
            return True
        if not s:
            return False
        
        if self.sameTree(s,t):
            return True
        
        return (self.sameTree(s.left, t) or self.sameTree(s.right, t))
        
        
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.left))
        
        return False  #if s is null and t is not null