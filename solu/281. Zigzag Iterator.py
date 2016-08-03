from collections import deque
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.tank = deque([])
        if v1: self.tank.append(v1[::-1])
        if v2: self.tank.append(v2[::-1])

    def next(self):
        """
        :rtype: int
        """
        n = self.tank.popleft()
        res = n.pop()
        if n: self.tank.append(n)
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.tank) > 0