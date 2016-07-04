class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cnt = 0
        while m != n:
            m, n, cnt = m>>1, n>>1, cnt+1
        return m<<cnt