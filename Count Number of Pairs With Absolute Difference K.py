class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        hashmap = defaultdict(int)  #good practice as {key:default value is 0}
        
        counter = 0
        
        for i in range(len(nums)):
            tmp1 = nums[i]-k
            tmp2 = nums[i]+k
            
            if tmp1 in hashmap:
                counter += hashmap[tmp1]
                
            if tmp2 in hashmap:
                counter += hashmap[tmp2]
                
            hashmap[nums[i]] += 1
            
        return counter