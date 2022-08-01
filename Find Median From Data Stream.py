class MedianFinder:

    def __init__(self):
        self.small, self.large = [] , []  #in python, heap can be defined just as list and do operation later

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1*num)  #Maxheap as small heap
        
        #make sure every element in small heap is less than every element in large heap
        if (self.small and self.large and (-1*self.small[0] > self.large[0])):
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #uneven size ?
        if len(self.small) > len(self.large) + 1:
            val = -1* heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        if len(self.large) > len(self.small) + 1:
            val = -1*heapq.heappop(self.large)
            heapq.heappush(self.small, val)
            
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-1*self.small[0] + self.large[0])/2
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        
        #Time Complexity - O(logn)  as adding or removing element in a heap takes logn time, we are not traversing any list we are calling the functions each time so no loops 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()