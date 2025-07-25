class Twitter:

    def __init__(self):
        # "userid": [tweetid]
        self.users = {}

        # "userid": [userid]
        self.followees = {}

        # tweet order
        # [tweetid]
        self.tweets = []
        

    def postTweet(self, userId, tweetId):
        if userId not in self.users:
            self.users[userId] = [tweetId]
        else:
            self.users[userId].append(tweetId)
        self.tweets.insert(0, tweetId)
        

    def getNewsFeed(self, userId):
        if userId not in self.followees:
            self.followees[userId] = [userId]

        tweets_to_get = []
        for user in self.followees[userId]:
            if user in self.users:
                tweets_to_get.extend(self.users[user])

        output = []
        for tweet in self.tweets:
            if tweet in tweets_to_get and len(output) < 10:
                output.append(tweet)

        return output
            
            
        

    def follow(self, followerId, followeeId):
        if followerId not in self.followees:
            self.followees[followerId] = [followerId, followeeId]
        else:
            self.followees[followerId].append(followeeId)
            
        

    def unfollow(self, followerId, followeeId):
        if followerId not in self.followees:
            self.followees[followerId] = [followerId]
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)


# Tests
from testsuite import lc_test

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

twitter = Twitter()
twitter.postTweet(1, 5)
lc_test(1, twitter.getNewsFeed(1), [5])
twitter.follow(1, 2)
twitter.postTweet(2, 6)
lc_test(2, twitter.getNewsFeed(1), [6, 5])
twitter.unfollow(1, 2)
lc_test(3, twitter.getNewsFeed(1), [5])

