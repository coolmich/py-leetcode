class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        w, wo = [-prices[0], max(-prices[0], -prices[1])], [0, max(0, prices[1] - prices[0])]
        for price in prices[2:]:
            w.append(max(w[-1], wo[-2] - price))
            wo.append(max(wo[-1], w[-2] + price))
        return wo[-1]
