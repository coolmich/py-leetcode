class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3): return False
        dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(1, len(s1)+1):
            if s1[:i] == s3[:i]: dp[i][0] = True
            else: break
        for j in range(1, len(s2)+1):
            if s2[:j] == s3[:j]: dp[0][j] = True
            else: break
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if i+j > len(s3): break
                if s1[i-1] == s3[i+j-1]: dp[i][j] |= dp[i-1][j]
                if s2[j-1] == s3[i+j-1]: dp[i][j] |= dp[i][j-1]
        return dp[-1][-1]