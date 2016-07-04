class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n:
            n -= 1
            m, n = n % 26, n / 26
            res.append(chr(65+m))
        return ''.join(res[::-1])