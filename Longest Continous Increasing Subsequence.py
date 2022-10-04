class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 1
        maximum = 1
        
        l = 0 
        
        while l+1 < len(nums):
            
            if nums[l+1] > nums[l]:
                longest += 1
            else:
                longest = 1
                
            maximum = max(longest,maximum)
            l += 1
            
        return maximum