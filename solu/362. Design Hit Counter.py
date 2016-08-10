from collections import deque
class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        t, c = timestamp, 0
        if self.q and self.q[-1][0] == timestamp:
            t, c = self.q.pop()
        self.q.append((t, c+1))

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.q and self.q[0][0] <= timestamp - 300: self.q.popleft()
        return sum([item[1] for item in self.q])

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)