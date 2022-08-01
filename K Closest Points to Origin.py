# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         minheap = []
        
#         #O(n) for this operation
#         for x, y in points:
#             dis = (x**2) + (y**2)
#             minheap.append([dis, x, y])  #O(1) operation
            
#         heapq.heapify(minheap)  # O(n) to build the heap
        
#         res = []
#         while k>0 :   #pop k times
#             dis , x, y = heapq.heappop(minheap)  
#             res.append([x,y]) 
#             k-= 1
            
#         return res

# # Heapify operation does NOT take nlogn time, it takes n time. So the overall complexity of the minheap solution is O(n + klogn) , whereas with sorting it's O(nlogn)





#Using maxheap
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]