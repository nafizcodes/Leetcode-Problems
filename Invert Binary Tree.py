https://leetcode.com/problems/invert-binary-tree/
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        #swap
        tmp = root.right
        root.right = root.left
        root.left = tmp
        
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root   