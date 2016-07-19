import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1: return 1
        res, mapi, h = [1], {}, []
        for p in primes:
            mapi[p] = 0
            heapq.heappush(h, (p, p))
        while len(res) < n:
            num, k = heapq.heappop(h)
            if num != res[-1]:
                res.append(num)
            mapi[k] += 1
            heapq.heappush(h, (k*res[mapi[k]], k))
        return res[-1]


print Solution().nthSuperUglyNumber(15, [3,5,7,11,19,23,29,41,43,47])