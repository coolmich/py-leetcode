class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def solve(stack):
            if len(stack) == n: return 1
            cnt = 0
            for i in range(n):
                if check(stack, i):
                    cnt += solve(stack + [i])
            return cnt
        def check(stack , i):
            for idx, item in enumerate(stack):
                if item == i or abs(i-item) == abs(len(stack) - idx): return False
            return True
        stack = []
        return solve(stack)