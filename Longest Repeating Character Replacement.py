# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         count = {}   # char : count
#         res = 0      
#         l = 0
        
#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r], 0)   #increase the count of char 
            
#             if (r - l + 1) - max(count.values()) > k:  #while can also be used
#                    count[s[l]] -= 1   #reduce the count in map
#                    l += 1   #shift the l pointer so shorten the length of substring
                   
            
#             res = max(res, r - l + 1)   #max between res and length 
                   
#         return res
    
    
    #Time complexity - O(26n)  - in worst case 26 diff chars so 26 times checking the hashmap for max freq
    #Space - O(n)
            

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}   # char : count
        res = 0      
        l = 0
        maxf = 0  #to store the maxf and check later if the num of char to be replaced is less than equal k
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)   #increase the count of char 
            maxf = max(maxf, count[s[r]])
            
            if (r - l + 1) - maxf > k:  #while can also be used
                   count[s[l]] -= 1
                   l += 1
                   
            
            res = max(res, r - l + 1)
                   
        return res

#Time  -- O(n)
#Space -- O(n)