class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return n
        a, b = 1, 2
        while n > 2:
            a, b, n = b, a+b, n-1
        return b
