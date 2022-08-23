class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i):
            
            if i >= len(nums) :
                res.append(subset.copy())
                
                return
            
            #we are taking in the index value
            subset.append(nums[i])
            dfs(i+1)
            
            
            #we are not taking the index value
            subset.pop()
            dfs(i+1)
            
            
        dfs(0)
      
        return res
    