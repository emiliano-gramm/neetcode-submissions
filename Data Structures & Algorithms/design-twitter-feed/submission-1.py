class Twitter:

    def __init__(self):
        self.posted = collections.defaultdict(list)
        self.followed = collections.defaultdict(list)
        self.latest = collections.deque()
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posted[userId].append(tweetId)
        self.latest.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        allowed = []
        res = []
        total = 0
        for followed in self.followed[userId]:
            if followed:
                allowed.append(followed)
        allowed.append(userId)
        for userId, postId in self.latest:
            if userId in allowed:
                res.append(postId)
                total += 1
            if total > 9:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        for i in range(len(self.followed[followerId])):
            if self.followed[followerId][i] == followeeId:
                self.followed[followerId][i] = None

        
