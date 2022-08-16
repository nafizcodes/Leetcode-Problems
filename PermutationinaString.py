class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1Count = {}
        s2Count = {}
        
        for i in range(len(s1)):
            s1Count[ord(s1[i])] = 1 + s1Count.get(ord(s1[i]) , 0)
            s2Count[ord(s2[i])] = 1 + s2Count.get((ord(s2[i] , 0)
            
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[s1[i]] == s2Count[s2[i]] else 0)
            
        l = 0
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            s2Count[r] += 1
            if s1Count[r] == s2Count[r]:
                matches += 1
            elif s1Count[r] + 1 == s2Count[r]:
                matches -= 1
                
            s2Count[l] -= 1
            if s1Count[l] == s2Count[l]:
                matches += 1
            elif s1Count[l] - 1 == s2Count[l]:
                matches -= 1
                
                