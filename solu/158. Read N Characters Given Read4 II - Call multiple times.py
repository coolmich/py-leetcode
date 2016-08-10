# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
from collections import deque

class Solution(object):
    def __init__(self):
        self.q = deque()

    def enq(self):
        if not self.q:
            buffer = ['']*4
            read4(buffer)
            for b in buffer:
                if b != '': self.q.append(b)

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        cnt = 0
        while cnt < n:
            self.enq()
            if not self.q: break
            buf[cnt] = self.q.popleft()
            cnt += 1
        return cnt