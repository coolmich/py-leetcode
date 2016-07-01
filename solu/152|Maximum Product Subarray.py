class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums): return 0
        maxL = minL = res = nums[0]
        for num in nums[1:]:
            val1, val2 = maxL*num, minL*num
            maxL, minL = max(max(val1, val2), num), min(min(val1, val2), num)
            res = max(maxL, res)
        return res