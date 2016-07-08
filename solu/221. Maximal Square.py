class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not len(matrix): return 0
        mat, maxi = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))], 0
        for c in range(len(matrix[0])):
            for r in range(len(matrix)):
                if not r or not c:
                    mat[r][c] = 1 if matrix[r][c] == '1' else 0
                else:
                    if matrix[r][c] == '1':
                        mat[r][c] = min(mat[r-1][c-1], mat[r][c-1], mat[r-1][c]) + 1
                maxi = max(maxi, mat[r][c])
        return maxi**2