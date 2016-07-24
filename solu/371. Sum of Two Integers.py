class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        def plus(d1, d2, c):
            if not c:
                if d1 and d2:
                    return (1, 0)
                elif (not d1 and d2) or (d1 and not d2):
                    return (0, 1)
                else:
                    return (0, 0)
            else:
                if d1 and d2:
                    return (1, 1)
                elif (not d1 and d2) or (d1 and not d2):
                    return (1, 0)
                else:
                    return (0, 1)
        c, res = 0, 0
        for i in range(32):
            mask = 1<<i
            c, d = plus(a&mask, b&mask, c)
            if d: res |= mask
        if res > 2**31:
            res -= 2**32
        return res