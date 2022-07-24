class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity   
        self.cache = {}  # hashmap - maps key to nodes
        
        #dummy nodes
        self.left , self.right = Node(0, 0) , Node(0, 0)  #left = LRU - least recently used , right = MRU  
        self.left.next , self.right.prev = self.right , self.left  
        #connect the two nodes so that we can insert in the middle

    #remove node from the list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
    #insert node at right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev
    
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val   #this gives the node
        return -1
    
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:   #if the key is in hashmap, then remove the key
            self.remove(self.cache[key])
        #if key not in hashmap or also after removing the existing key
        self.cache[key] = Node(key, value)  #make a new node for the new key
        self.insert(self.cache[key]) #insert the node in the MRU
        
        if len(self.cache) > self.cap:
            #remove and delete the LRU from the hashmap
            lru = self.left.next  #we have left pointer for this,     left(LRU) -> [2,2] -> [1,1] -> [3,3] -> right(MRU)
            self.remove(lru)  #remove from linked list 
            del self.cache[lru.key]  #remove from the hashmap
            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)