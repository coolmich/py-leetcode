class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, dp = sorted(nums), [0] * (target+1)
        dp[0] = 1
        for i in range(target+1):
            j = 0
            while j < len(nums) and nums[j] <= i:
                dp[i] += dp[i-nums[j]]
                j += 1
        return dp[-1]