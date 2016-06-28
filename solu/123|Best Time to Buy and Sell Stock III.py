class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not len(prices): return 0
        l_min, l_maxp, l_li, r_max, r_maxp, r_li = prices[0], 0, [], prices[-1], 0, []
        for p in prices:
            l_min = min(l_min, p)
            l_maxp = max(l_maxp, p - l_min)
            l_li.append(l_maxp)
        for p in prices[::-1]:
            r_max = max(r_max, p)
            r_maxp = max(r_maxp, r_max - p)
            r_li.append(r_maxp)
        return max([l_li[i]+r_li[len(r_li)-1-i] for i in range(len(l_li))])
