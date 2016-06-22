class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        startr, endr, row = 0, len(matrix)-1, -1
        while startr < endr - 1:
            mid = (startr + endr) / 2
            if matrix[mid][0] == target:
                row = mid
                break
            elif matrix[mid][0] < target:
                startr = mid
            else:
                endr = mid - 1
        if row == -1:
            if target < matrix[startr][0]:
                row = startr - 1
            elif target >= matrix[endr][0]:
                row = endr
            else:
                row = startr
        if row == -1: return False
        start, end = 0, len(matrix[0]) - 1
        while start < end:
            mid = (start+end)/2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return matrix[row][start] == target