"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph (self, node: 'Node') -> 'Node':
        oldToNew = {}  #hashmap to {old : clone}
        
        def dfs (node):
            
            if not node:
                return None 
            
            #check if the clone exists or not, if exists: return the node
            if node in oldToNew:      
                return oldToNew [node]

            #if clone does not exist, first make copy of the node and then add the clone to the graph
            copy = Node(node.val)  #making a clone here
            
            oldToNew[node] = copy  #putting the clone against original value in hashmap

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node)
    
    
#Time complexity = O(n) ~ O(E+V) 
# We have to make clone of each nodes so total number of edges and vertices 
