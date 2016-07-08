from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = deque([])
        self.sz = 0


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)
        self.sz += 1
        n = self.sz
        while n > 1:
            self.q.append(self.q.popleft())
            n -= 1

    def pop(self):
        """
        :rtype: nothing
        """
        self.sz -= 1
        self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return self.sz == 0
        