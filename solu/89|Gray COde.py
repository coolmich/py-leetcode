class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0: return [0]
        if n == 1: return [0, 1]
        arr, base = self.grayCode(n-1), 1<<(n-1)
        return arr + [(base+item) for item in reversed(arr)]