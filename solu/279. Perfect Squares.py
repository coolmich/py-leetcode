class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        res = [0, 1]
        for i in range(2, n+1):
            j, mini = 1, 2**31
            while j**2 <= i:
                mini = min(mini, 1 + res[i - j**2])
                j += 1
            res.append(mini)
        return res[-1]
print Solution().numSquares(7334)