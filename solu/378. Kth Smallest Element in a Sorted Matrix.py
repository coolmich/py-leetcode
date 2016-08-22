import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap, cnt = [], 0
        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[0][i], (0, i)))
        while cnt < k:
            val, (r, c) = heapq.heappop(heap)
            if r < len(matrix) - 1: heapq.heappush(heap, (matrix[r+1][c], (r+1, c)))
            cnt += 1
        return val