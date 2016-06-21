class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not r and not c:
                    continue
                elif not r:
                    grid[r][c] += grid[r][c-1]
                elif not c:
                    grid[r][c] += grid[r-1][c]
                else:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        return grid[-1][-1]