class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        #Brute force Time - O(n^2)
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 print(nums[i], nums[j])
#                 if nums[i] == nums[j]:
#                     count += 1
                    
#         return count
    
    
        
        
        counter = 0
        hashmap = {}
        
        
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
                
            else:
                counter += hashmap[nums[i]]
                
                hashmap[nums[i]] += 1
                
                
                
        return counter
        
        
        Time - O(n)
        Spsce - O(n)
    