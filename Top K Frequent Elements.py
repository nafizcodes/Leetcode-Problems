class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] = 1 + count.get(n,0) #to form the hashmap of count of each value 
            #{1:3, 2:2, 3:1}
            
        for n,c in count.items(): #to populate the freq array with values corresponding to the count(which is the                                                                                                           index here)
            freq[c].append(n)
            #[[],[3],[2],[1],[],[]]
            
        res = []
        
        for n in range(len(freq)-1 , 0, -1):
            for i in freq[n]:
                res.append(i)
                if len(res) == k:
                    return res
        
        