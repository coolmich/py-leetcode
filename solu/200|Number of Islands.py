class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def visit(grid, r, c):
            if grid[r][c] == '1':
                grid[r][c] = '0'
                if r > 0:
                    visit(grid, r-1, c)
                if r < len(grid)-1:
                    visit(grid, r+1, c)
                if c > 0:
                    visit(grid, r, c-1)
                if c < len(grid[0])-1:
                    visit(grid, r, c+1)
        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    visit(grid, r, c)
                    cnt += 1
        return cnt