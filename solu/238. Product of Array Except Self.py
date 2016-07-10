class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        res = [1] * len(nums)
        num1 = nums[0]
        for i in range(1, len(nums)):
            res[i] *= num1
            num1 *= nums[i]
        num1 = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= num1
            num1 *= nums[i]
        return res