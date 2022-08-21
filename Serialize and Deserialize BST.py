# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        return ' '.join(map(str, vals))

    # O( N ) since each val run build once
    def deserialize(self, data):
        vals = [int(val) for val in data.split()]

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.pop(0)
                node = TreeNode(val)
                
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                
                return node

        return build(float('-infinity'), float('infinity'))

        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans