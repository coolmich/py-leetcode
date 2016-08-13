class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 3:
            return []

        res = []
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                res.append([i, n/i])
                res += [[i] + r for r in self.getFactors(n/i) if r[0] >= i]

        return res
        