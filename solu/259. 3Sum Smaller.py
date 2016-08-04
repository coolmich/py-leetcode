class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def twoSumSmaller(nums, target):
            l, r, res = 0, len(nums) - 1, 0
            while l < r:
                if nums[l] + nums[r] >= target: r -= 1
                else: res, l = res+r-l, l+1
            return res
        nums, res = sorted(nums), 0
        for i in range(len(nums)):
            res += twoSumSmaller(nums[i+1:], target-nums[i])
        return res