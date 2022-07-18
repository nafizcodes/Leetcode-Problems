class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
# preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#  mid = 3
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid+1] , inorder[ : mid+1])
        root.right = self.buildTree(preorder[mid+1 : ], inorder[mid+1 : ])
        
        return root