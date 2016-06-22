class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r_, c_ = False, False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if not matrix[r][c]:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    if not r: r_ = True
                    if not c: c_ = True
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if not matrix[r][0] or not matrix[0][c]:
                    matrix[r][c] = 0
        if c_:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        if r_:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
    