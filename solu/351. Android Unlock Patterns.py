class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def is_valid(r1, c1, r2, c2, grid):
            r_d, c_d = abs(r1-r2), abs(c1-c2)
            if (r_d, c_d) in [(2,0), (0,2)]:
                if r1 == r2: return grid[r1][(c1+c2)/2]
                elif c1 == c2: return grid[(r1+r2)/2][c1]
            elif (r_d, c_d) == (2,2):
                return grid[1][1]
            return True
        def visit(r, c, grid, cum, m, n, res):
            grid[r][c] = 1
            cum += 1
            if m<=cum<=n: res[0] += 1
            if cum < n:
                for r_ in range(3):
                    for c_ in range(3):
                        if not grid[r_][c_] and is_valid(r, c, r_, c_, grid): visit(r_, c_, grid, cum, m, n, res)
            grid[r][c] = 0


        grid, ret = [[0 for i in range(3)] for j in range(3)], []
        for r,c in [(0,0), (0,1), (1,1)]:
            res = [0]
            visit(r, c, grid, 0, m, n, res)
            ret += res
        return ret[0]*4 + ret[1]*4 + ret[2]