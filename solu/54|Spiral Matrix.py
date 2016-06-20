class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not len(matrix): return []
        y, x = 0, 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direc, stack, n = 0, [matrix[y][x]], 1
        matrix[y][x] = None
        while n < len(matrix)*len(matrix[0]):
            y_, x_ = direction[direc]
            yy, xx = y+y_, x+x_
            if yy < 0 or yy >= len(matrix) or xx < 0 or xx >= len(matrix[0]) or matrix[yy][xx] is None:
                direc = (direc+1) % 4
            else:
                stack.append(matrix[yy][xx])
                matrix[yy][xx], n, y, x = None, n+1, yy, xx
        return stack
