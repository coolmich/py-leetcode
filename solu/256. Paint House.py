class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        dp = [[0 for i in range(3)] for j in range(len(costs))]
        dp[0][:] = costs[0][:]
        for i in range(1, len(costs)):
            for j in range(3):
                dp[i][j] = min(dp[i-1][:j] + dp[i-1][j+1:]) + costs[i][j]
        return min(dp[-1])