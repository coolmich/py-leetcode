class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        stack = [1] * n
        while m > 1:
            for i in range(1, n):
                stack[i] += stack[i-1]
            m -= 1
        return stack[-1]