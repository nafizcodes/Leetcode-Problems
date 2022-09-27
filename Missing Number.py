class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         sum = (n * (n+1))//2
#         for num in nums:
#             sum = sum - num

#         return sum
    
#         sum = len(nums)   #starts with len(nums) because in the for loop, the last index is not included
#         for i in range(len(nums)):  #we cannot do len(nums)+1 because nums will be out of range
#             sum = sum + i - nums[i]
            
#         return sum
    
        res = len(nums)   #or else starting w 0 does not eliminate the value of len(nums) if it exists
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]
        return res