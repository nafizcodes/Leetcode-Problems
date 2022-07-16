class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        longest = 0
        numSet = set(nums)
        for n in nums:
            if n-1 not in numSet:
                #check next element of n
                next = n+1 
                
                while next in numSet:
                    next += 1
                    
                longest = max(longest, next - n )
        
        return longest
                    