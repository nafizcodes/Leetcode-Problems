class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
    
        
        count = Counter(tasks)  #Counter({'A': 3, 'B': 3})
        
        maxHeap = [-i for i in count.values()]   #dict_values([3, 3])  #maxHeap = [-3, -3]  
        #using maxheap to determine which task is how many times
         
        heapq.heapify(maxHeap)  
        
        time = 0
        queue = deque() # pairs of [-count, idleTime]
        
        while maxHeap or queue: 
            time += 1
            
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
            
                if cnt:   #if cnt is not zero add to the queue for later
                    queue.append([cnt, time + n])   #time + idle time  to update in the queue
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
                
        return time
                
                
        
        
            #Time Complexity - O(n)  #Space - O(n) heapify n elements
 # Generally it takes logn for push pop but here its log26 as only 26 letters so constant time to determine which letter is most frequent
        #However, if tasks = [A, A, A, A] , then it will take idle time for each so O(n*m) where m is the idle time