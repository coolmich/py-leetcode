class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        mark = [False] * (n+1)
        # mark even
        for i in xrange(4, n+1, 2):
            mark[i] = True
        # the rest
        for i in xrange(3, n+1):
            if i**2 > n: break
            if not mark[i]:
                for j in xrange(i*2, n+1, i):
                    mark[j] = True
        cnt = 0
        for i in range(2, n):
            if not mark[i]: cnt += 1
        return cnt