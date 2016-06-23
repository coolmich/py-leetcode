class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k: return []
        if n == k: return [list(range(1, n+1))]
        if k == 1:
            return [[i] for i in range(1, n+1)]
        res = []
        for i in range(n, 0, -1):
            arr = self.combine(i-1, k-1)
            if arr:
                for li in arr:
                    li.append(i)
                res += arr
        return res
