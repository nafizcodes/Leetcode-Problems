class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, n in enumerate(nums):   # we wanna use each number as the first possible value
            if i > 0 and n == nums[i-1]: # we dont wanna use same value as the first value
                continue
                
            l, r = i + 1 , len(nums) - 1   # pointers to do two sum for the rest of the list
            
            while l < r:
                threeSum = n + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l] , nums[r]])
                    
                    # [ -2, -2 , 0 , 0, 2, 2]
                    l += 1         #alternate r -= 1
                    while nums[l] == nums[l+1] and l < r:  #while the current l and prev val of l is equal, increment l  | alternate with r can also be done
                        l += 1
                        
                #We donot need to check for both sides as the outer loop checks for the sum and works respectively
                    
        return res
    
    
    #Time O(nlgn) + O(n^2) , Hence, O(n^2)
    #Space O(1) , however O(n) in cases where sorting might take some memory