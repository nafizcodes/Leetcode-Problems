class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  #kth largest element if the array was sorted
        
        def quickSelect(l, r):
            pivot = nums[r]
            pointer = l  #pointer at the left as shown in diagram
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer]   #swap the elements
                    pointer += 1    # increment pointer
                    
                # if greater than pivot we do nothing as the above condition will already sort accordingly
            
            nums[pointer], nums[r] = nums[r], nums[pointer]     
            
            if pointer > k :
                return quickSelect(l, pointer - 1)
            elif pointer < k:
                return quickSelect(pointer+1, r)
            else:
                return nums[pointer]
            
            
#         return quickSelect(0, len(nums)-1)

#Time Complexity - O(n)
            
        
        
# ✔️ Solution 1: MinHeap

# We use minHeap to keep up to k smallest elements of the nums array.
# Then top of the minHeap is the k largest element.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for x in nums:        #n times
            heappush(minHeap, x)    
            if len(minHeap) > k:
                heappop(minHeap)   #log k
# Complexity:

# Time: O(NlogK)
# Space: O(K)


# ✔️ Solution 2: MaxHeap

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-x for x in nums]
        heapify(maxHeap)      # O(n) time

        
        for i in range(k-1):    #k times
            heappop(maxHeap)   #logn   so #time -> O(klogn)
        return -maxHeap[0]
# Complexity:

# Time: O(N + KlogN), heapify cost O(N), heappop k times costs O(KlogN).
# Space: O(N)

        
        
# Sorting approach  -- O(nlogn)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)- k]
         
    