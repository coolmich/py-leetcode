class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1: return 1
        res, n2, n3, n5 = [1], 0, 0, 0
        while len(res) < n:
            mini = min(res[n2]*2, min(res[n3]*3, res[n5]*5))
            if mini == res[n2]*2: n2 += 1
            elif mini == res[n3]*3: n3 += 1
            else: n5 += 1
            if mini != res[-1]:
                res.append(mini)
        return res[-1]
