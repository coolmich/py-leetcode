class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return 1
        li = [0] * (n+1)
        li[0] = li[1] = 1
        for i in range(2, n+1):
            res = 0
            for j in range(i):
                res += li[j]*li[i-1-j]
            li[i] = res
        return li[-1]