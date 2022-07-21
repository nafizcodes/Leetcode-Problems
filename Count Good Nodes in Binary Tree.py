# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def preorder(node, maxval):
            
            if not node:
                return 0
            
            
            
            if node.val >= maxval:
                num = 1
            else:
                num = 0
            
            maxval = max(maxval, node.val)
                
            num += preorder(node.left, maxval)
            num += preorder(node.right, maxval)
            
            return num
        
        return preorder(root, root.val)
            