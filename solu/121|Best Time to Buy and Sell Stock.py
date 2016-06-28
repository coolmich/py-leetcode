class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not len(prices): return 0
        run_min = prices[0]
        max_profit = 0
        for price in prices:
            run_min = min(run_min, price)
            max_profit = max(price-run_min, max_profit)
        return max_profit