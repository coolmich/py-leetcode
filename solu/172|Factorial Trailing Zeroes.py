class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        base, res = 5, 0
        while n/base:
            res, base = res+n/base, base*5
        return res