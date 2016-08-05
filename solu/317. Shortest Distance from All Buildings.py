from collections import defaultdict, deque
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def explore(r, c, grid, mapi):
            dp = [[2**31-1 for i in range(len(grid[0]))] for j in range(len(grid))]
            dp[r][c], q = 0, deque([(r, c)])
            while q:
                r, c = q.popleft()
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    row, col = r+x, c+y
                    if 0<=row<len(grid) and 0<=col<len(grid[0]) and not grid[row][col] and dp[row][col] > dp[r][c]+1:
                        dp[row][col] = dp[r][c]+1
                        q.append((row, col))
                        mapi[(row, col)].append(dp[row][col])
        stack, mapi = [], defaultdict(list)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: stack.append((r,c))
        for r, c in stack:
            explore(r, c, grid, mapi)
        mini = 2**31-1
        for k in mapi:
            if len(mapi[k]) == len(stack): mini = min(mini, sum(mapi[k]))
        return -1 if mini == 2**31-1 else mini