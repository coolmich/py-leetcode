class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, res = 0, 0
        while i < 32:
            if n & (1 << i): res += 1
            i += 1
        return res