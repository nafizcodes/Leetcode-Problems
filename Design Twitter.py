class Twitter:

    def __init__(self):
        self.count = 0  #time to determine recent post
        self.followMap = defaultdict(set)   #userId-> set of followeeId
        self.tweetMap = defaultdict(list)    #userId -> list of [count, tweetIds]
        
        
        #save couple lines of code using default dict 
        #otherwise implementation will be:
        #self.followMap = {}
        #then in follow function: 
        #self.followMap[followerId] = set
        #self.followMap[followerId].add(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        
        self.followMap[userId].add(userId)   #user is following themselves sowe add the user itself to the followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1 ])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
            #if the person has more tweets
            #count to order the tweets, tweetId to add to the res, followee to mark of the fo
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #if the follower is following the followeeId then remove it
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)