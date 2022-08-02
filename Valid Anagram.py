class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) time, O(n) space
        charCounts = {}
        
        for c in s:
            charCounts[c] = charCounts.get(c, 0) + 1
        for c in t:
            charCounts[c] = charCounts.get(c, 0) - 1
        
        for c in charCounts:
            if charCounts[c] != 0:
                return False
        return True