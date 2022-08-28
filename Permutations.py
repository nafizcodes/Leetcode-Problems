class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        for i in nums:
            #base case if len is 1 then, return the nums
            if (len(nums) == 1):
                return [nums[:]]
            
            #if not base case, pop the first element and call permute on the rest of the nums array
            n = nums.pop(0)
            perms = self.permute(nums)  
            
            #for each oermutations in each level, append the n
            for p in perms:
                p.append(n)
                
            
            result.extend(perms)  #extend add multiple items to the list
            nums.append(n) #this adds the n back to the nums for next iteration
            
        return result
            
                