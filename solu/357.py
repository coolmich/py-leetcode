class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n: return 1
        n, res = min(n, 10), 10
        for i in range(2, n+1):
            tmp = 9
            for j in range(9, 10-i, -1):
                tmp *= j
            res += tmp
        return res
    