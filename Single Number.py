class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0
        
        for n in nums:
            res = res ^ n
            
        return res
        
        
        
        
        
        
        
        
# def singleNumber1(self, nums):
#     dic = {}
#     for num in nums:
#         dic[num] = dic.get(num, 0)+1
#     for key, val in dic.items():
#         if val == 1:
#             return key
    
# def singleNumber4(self, nums):
#     return reduce(lambda x, y: x ^ y, nums)