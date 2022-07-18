# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def longestpathDFS(node):
            if not node:
                return 0
            
            left = longestpathDFS(node.left)
            right = longestpathDFS(node.right)
            
            nonlocal diameter
            diameter = max(diameter, left + right) 
            
            return 1 + max(left,right)
        
        longestpathDFS(root)
        return diameter
        
        
#        1
#       / \
#      2   3
#     / \
#    4   5
# diameter 3