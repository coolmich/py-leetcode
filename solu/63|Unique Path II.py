class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        mat = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1: break
            mat[0][i] = 1
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1: break
            mat[i][0] = 1
        for r in range(1, len(obstacleGrid)):
            for c in range(1, len(obstacleGrid[0])):
                mat[r][c] = (mat[r-1][c] if not obstacleGrid[r-1][c] else 0) + (mat[r][c-1] if not obstacleGrid[r][c-1] else 0)
        return mat[-1][-1] if not obstacleGrid[-1][-1] else 0