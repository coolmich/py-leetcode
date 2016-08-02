class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def draw(stack):
            pic = [['.' for j in range(len(stack))] for i in range(len(stack))]
            for idx, item in enumerate(stack):
                pic[idx][item] = 'Q'
            return [''.join(item) for item in pic]
        def solve(stack, res):
            if len(stack) == n:
                res.append(draw(stack))
                return
            for i in range(n):
                if check(stack, i):
                    solve(stack + [i])
        def check(stack , i):
            for idx, item in enumerate(stack):
                if item == i or abs(i-item) == abs(len(stack) - idx): return False
            return True

        stack, res = [], []
        return res

print Solution().solveNQueens(4)