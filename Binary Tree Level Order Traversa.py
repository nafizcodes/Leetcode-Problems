# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #need to make a sublist to store each level nodes
        #need to make a result list to store the sublists of each level
        #bfs - queue - to traverse level by level
        
        res = []
        
        q = deque([root])
        
        while q: 
            qlen = len(q)
            level = []

            for i in range(qlen):
                node = q.popleft()  #iteration 1.q = [3]  2.[9,20] 3.[20] 4.[15,7] 5.[0]

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)
            
        return res
                