class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
#         product = 1
        
#         for n in nums:
#             product *= n
        
#         return self.signFunc(product)
    
    
#     def signFunc(self,x):
#         if x > 0 :
#             return 1
#         elif x < 0 :
#             return -1
#         else:
#             return 0
            
        count = 0
        for n in nums:
            if n == 0:
                return 0
            
            if n < 0:
                count += 1
        
        if count % 2 == 0:
            return 1
        else:
            return -1