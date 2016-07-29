class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0

        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        def traverse(matrix, r, c, dp):
            if dp[r][c]: return dp[r][c]
            if r > 0 and matrix[r - 1][c] > matrix[r][c]:
                dp[r][c] = max(dp[r][c], traverse(matrix, r - 1, c, dp))
            if r < len(matrix) - 1 and matrix[r + 1][c] > matrix[r][c]:
                dp[r][c] = max(dp[r][c], traverse(matrix, r + 1, c, dp))
            if c > 0 and matrix[r][c - 1] > matrix[r][c]:
                dp[r][c] = max(dp[r][c], traverse(matrix, r, c - 1, dp))
            if c < len(matrix[0]) - 1 and matrix[r][c + 1] > matrix[r][c]:
                dp[r][c] = max(dp[r][c], traverse(matrix, r, c + 1, dp))
            dp[r][c] += 1
            return dp[r][c]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                traverse(matrix, r, c, dp)
        return max(map(max, dp))