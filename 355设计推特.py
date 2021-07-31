class user:
    def __init__(self):
        self.followees = {}
        self.tweets = []


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.tweetTime = {}
        self.recentMax = 0
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.users.keys():
            self.users[userId] = user()
        self.users[userId].tweets.append(tweetId)
        self.tweetTime[tweetId] = self.time
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.users.keys():
            return []
        mine = self.users[userId].tweets[-10:]
        combine = []

        for followee in self.users[userId].followees.keys():
            others = self.users[followee].tweets[-10:]
            i, j = 0, 0
            while (i + j < 10 and (len(mine) + len(others) > 0)):
                if len(mine) and len(others):
                    if self.tweetTime[mine[-1]] > self.tweetTime[others[-1]]:
                        combine.append(mine.pop())
                        i += 1
                    else:
                        combine.append(others.pop())
                        j += 1
                elif len(mine) == 0:
                    combine.append(others.pop())
                    j += 1
                elif len(others) == 0:
                    combine.append(mine.pop())
                    i += 1

            mine = combine[:10]
            combine = []
            mine.reverse()
        mine.reverse()

        return mine

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        if followerId not in self.users.keys():
            self.users[followerId] = user()
        if followeeId not in self.users.keys():
            self.users[followeeId] = user()
        self.users[followerId].followees[followeeId] = self.users[followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users.keys() or followeeId not in self.users.keys():
            return
        if followeeId not in self.users[followerId].followees.keys():
            return
        self.users[followerId].followees.pop(followeeId)



        # Your Twitter object will be instantiated and called as such:
        # obj = Twitter()
        # obj.postTweet(userId,tweetId)
        # param_2 = obj.getNewsFeed(userId)
        # obj.follow(followerId,followeeId)
        # obj.unfollow(followerId,followeeId)