class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10,15,20] add 0
        
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            #cost[i] = min(cost[i+1] + cost[i], cost[i+2] + cost[i])
            cost[i] += min(cost[i+1] , cost[i+2] )
            
        return min(cost[0], cost[1])   #guranteed min length of cost array is 2