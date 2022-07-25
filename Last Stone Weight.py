class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
            
        while len(stones) > 1:
            first = heapq.heappop(stones)   
            second = heapq.heappop(stones)
                
            if second > first:   #as we are doing negative values, second is greater #example , -7 > -8 
                heapq.heappush(stones, first - second)  # -8 -(-7) = -1
                    #we can also do -1*(second - first)
                    
        stones.append(0)
            
        return abs(stones[0])   #abs(heapq.heappop(stones))
                