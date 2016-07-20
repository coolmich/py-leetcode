class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        INF = 0x7FFFFFFF
        dp, i = [0] + [INF]*amount, 0
        while i < len(dp):
            if dp[i] != INF:
                for coin in coins:
                    if i + coin <= amount:
                        dp[i+coin] = min(dp[i+coin], dp[i] + 1)
            i += 1
        return -1 if dp[-1] == INF else dp[-1]