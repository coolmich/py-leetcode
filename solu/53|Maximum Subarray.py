class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums): return 0
        maxSum = nums[0]
        prevM = nums[0]
        for num in nums[1:]:
            prevM = max(num + prevM, num)
            maxSum = max(maxSum, prevM)
        return maxSum
        