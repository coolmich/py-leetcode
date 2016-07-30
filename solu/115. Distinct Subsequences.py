class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # dp[i,j]: s[:i] -> t[:j]
        dp = [[0 if j else 1 for j in range(len(t)+1)] for i in range(len(s)+1)]
        for ti in range(1, len(t)+1):
            for si in range(ti, len(s)+1):
                if t[ti-1] == s[si-1]:
                    dp[si][ti] += dp[si-1][ti-1]
                dp[si][ti] += dp[si-1][ti]
        return dp[-1][-1]