class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        
        l = 0
        
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
                
            charSet.add(s[r])
            
            res = max(res, r - l + 1)
            
        return res
            
        
        # Time Complexity - O(n)    travers the entire string
        # Space Complexity - O(n)  - set used to store - worst case where each char might be different and we need to add all of them