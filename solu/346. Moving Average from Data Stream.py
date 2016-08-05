from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = deque()
        self.c = size
        self.sumi = 0.0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.q) == self.c:
            self.sumi -= self.q.popleft()
        self.sumi += val
        self.q.append(val)
        return self.sumi/len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)