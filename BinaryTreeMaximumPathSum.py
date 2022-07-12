# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        #return the max sum without split 
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            #we check the left and right max for negative values
            leftMax = max(leftMax, 0)  
            rightMax = max(rightMax, 0)
            
            #to compute the max path sum with split to update the res value
            res[0] = max(res[0] , root.val + leftMax + rightMax)
            
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
            
            