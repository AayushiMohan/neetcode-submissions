import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}       # userId -> [(time, tweetId)]
        self.following = {}    # userId -> set of followees

    def postTweet(self, userId, tweetId):
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        heap = []

        # User's own tweets
        users = {userId}

        # Users they follow
        if userId in self.following:
            users.update(self.following[userId])

        # Put each user's latest tweet into heap
        for user in users:
            if user in self.tweets:
                tweets = self.tweets[user]
                index = len(tweets) - 1

                time, tweetId = tweets[index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        result = []

        while heap and len(result) < 10:
            negTime, tweetId, user, index = heapq.heappop(heap)

            result.append(tweetId)

            # Get this user's previous tweet
            index -= 1

            if index >= 0:
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        return result

    def follow(self, followerId, followeeId):
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.following:
            self.following[followerId].discard(followeeId)