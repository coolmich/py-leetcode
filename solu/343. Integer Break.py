class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr, pattern = [1,2,4], [6,9,12]
        if n > 4:
            return 3**((n-5)/3) * pattern[(n-5)%3]
        else:
            return arr[n-2]