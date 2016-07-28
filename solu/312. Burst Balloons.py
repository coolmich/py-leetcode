class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums = [1] + nums + [1]
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for gp in range(len(nums)-2):
            for start in range(1, len(nums)-1):
                end, maxi = start + gp, 0
                if end >= len(nums)-1: break
                for i in range(start, end+1):
                    dp[start][end] = max(dp[start][end], dp[start][i-1] + dp[i+1][end] + nums[i]*nums[start-1]*nums[end+1])
        return dp[1][-2]
