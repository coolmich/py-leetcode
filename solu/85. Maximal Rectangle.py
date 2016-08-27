class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        dp = [[(0,0) for i in range(len(matrix[0]))] for j in range(len(matrix))]
        if matrix[0][0]: dp[0][0] = (1,1)
        for i in range(1, len(matrix)):
            if matrix[i][0] == '1': dp[i][0] = (1, dp[i-1][0][1]+1)
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == '1': dp[0][i] = (dp[0][i-1][0]+1, 1)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    w1, h1 = dp[i-1][j]
                    w2, h2 = dp[i][j-1]
                    dp[i][j] = (min(w2+1, w1), min(h1+1, h2))
        return max([dp[i][j][0]*dp[i][j][1] for i in range(len(dp)) for j in range(len(dp[0]))])
print Solution().maximalRectangle(["10100","10111","11111","10010"])