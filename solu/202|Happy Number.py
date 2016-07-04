class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_d(n):
            res = []
            while n:
                res.append(n%10)
                n/=10
            return res[::-1]
        seen = set([])
        while n != 1:
            if n in seen: return False
            seen.add(n)
            n = sum([d**2 for d in get_d(n)])
        return True