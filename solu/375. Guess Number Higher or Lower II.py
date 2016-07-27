class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end, dp = 1, n, [[0 for i in range(n+1)] for j in range(n+1)]
        for gp in range(1, n):
            for start in range(1, n):
                end = start + gp
                if end > n: break
                dp[start][end] = min([(max(dp[start][k-1], dp[k+1][end]) + k) for k in range(start, end)])
        return dp[1][n]