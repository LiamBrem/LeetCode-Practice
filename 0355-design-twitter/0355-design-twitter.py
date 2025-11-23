from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followings = defaultdict(set)
        self.timeId = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.timeId, tweetId))
        self.timeId += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        li = []
        for followee in self.followings[userId]:
            for tweet in self.tweets[followee]:
                li.append(tweet)

        for tweet in self.tweets[userId]:
            li.append(tweet)

        heapq.heapify(li)
        res = []
        for i in range(10):
            if li:
                res.append(heapq.heappop(li)[1])
            else:
                break

        return res
            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followings[followerId]:
            self.followings[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)