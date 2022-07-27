class KthLargest:
    
    #constructor
    def __init__(self, k: int, nums: List[int]): 
        #initializing the members
        self.minHeap , self.k = nums, k
        heapq.heapify(self.minHeap)  #forming the heap
        while len(self.minHeap) > k:    #continue to pop until the len of heap is equal to k
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        #adding the val to the heap
        heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > self.k:  #if len of heap is greater than k then pop - the heap might be less than k size
            heapq.heappop(self.minHeap)
        return self.minHeap[0]    #returning the min element as this is the kth largest in a length of k elements
        
        
#Time Complexity - for add => O(mlogn) --- logn to add and m times we call add function

# the work for heap sort is the sum of the two stages: O(n) time for buildHeap and O(n log n) to remove each node in order, so the complexity is O(n log n).
#  for constructor - O(nlogn) --- logn to pop element and (n-k) times ~ n times (n-k as we pop until we have k elements)
    
#Space Complexity -  Since Heapify is a recursive function, its space complexity is O(logn) because of the stack space required for recursion.

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)