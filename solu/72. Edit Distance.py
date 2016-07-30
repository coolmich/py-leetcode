class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #dp[i,j]: word1[:i] -> word2[:j]
        dp = [[0 if i else j for i in range(len(word2)+1)] if j else [k for k in range(len(word2)+1)] for j in range(len(word1)+1)]
        for j in range(1,len(word2)+1):
            for i in range(1,len(word1)+1):
                if word2[j-1] == word1[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
        return dp[-1][-1]