class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()  #sorting as we check present and next int for duplicates
        
        
        def backtrack(i, subset):
            
            #base case
            if i == len(nums):

                res.append(subset.copy())   #also subset([::]) is valid
                
                return
            
            
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
                
            backtrack(i+1, subset)
            
        backtrack(0, [])
        
        return res
            
            