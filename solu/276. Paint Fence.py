class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if not n or not k: return 0
        dp, dp_rep = [[0 if j else 1 for i in range(k)] for j in range(n)], [[0 for i in range(k)] for j in range(n)]
        for i in range(1, n):
            tmp = sum(dp[i-1][:])
            tmp1 = sum(dp_rep[i-1][:])
            for j in range(k):
                dp[i][j] = tmp - dp[i-1][j] + tmp1 - dp_rep[i-1][j]
            dp_rep[i][:] = dp[i-1][:]
        return sum(dp[-1][:]) + sum(dp_rep[-1][:])
