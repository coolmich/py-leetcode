class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        depth = len(matrix) / 2
        n = 0
        while n < depth:
            y = n
            for x in range(n, len(matrix)-1-n):
                y2, x2 = self.calc_target(len(matrix), (y, x))
                y3, x3 = self.calc_target(len(matrix), (y2, x2))
                y4, x4 = self.calc_target(len(matrix), (y3, x3))
                matrix[y][x], matrix[y2][x2], matrix[y3][x3], matrix[y4][x4] = matrix[y4][x4], matrix[y][x], matrix[y2][x2], matrix[y3][x3]
            n += 1

    def calc_target(self, n, src_tup):
        y, x = src_tup
        return x, n-y-1
