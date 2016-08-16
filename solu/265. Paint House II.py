class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        dp = [[0 for i in range(len(costs[0]))] for j in range(len(costs))]
        dp[0][:] = costs[0][:]
        for i in range(1, len(costs)):
            mini = min(dp[i-1])
            dp[i] = [mini] * len(dp[i])
            min_idx = dp[i-1].index(mini)
            dp[i][min_idx] = min(dp[i-1][:min_idx]+dp[i-1][min_idx+1:])
            dp[i] = [a+b for a, b in zip(dp[i], costs[i])]
        return min(dp[-1])