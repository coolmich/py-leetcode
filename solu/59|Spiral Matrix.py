class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mat = [[0 for i in range(n)] for j in range(n)]
        depth, cnt = 0, 1
        while depth < (n+1)/2:
            y, x = depth, depth
            if cnt == n**2:
                mat[y][x] = cnt
                return mat
            for x in range(x, n-depth-1):
                mat[y][x], cnt = cnt, cnt + 1
            x += 1
            for y in range(y, n-depth-1):
                mat[y][x], cnt = cnt, cnt + 1
            y += 1
            for x in range(x, depth, -1):
                mat[y][x], cnt = cnt, cnt + 1
            x -= 1
            for y in range(y, depth, -1):
                mat[y][x], cnt = cnt, cnt + 1
            depth += 1
        return mat