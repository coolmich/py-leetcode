class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.cache = [[0 for i in range((len(matrix[0]) if matrix else 0) +1)] for j in range(len(matrix)+1)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.cache[r+1][c+1] = self.cache[r+1][c] + self.cache[r][c+1] - self.cache[r][c] + matrix[r][c]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.cache[row2+1][col2+1] - self.cache[row2+1][col1] - self.cache[row1][col2+1] + self.cache[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)