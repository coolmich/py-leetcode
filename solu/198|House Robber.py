class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums): return 0
        if len(nums) < 2:
            return nums[0]
        res = nums[:2]
        for i in range(2, len(nums)):
            if i == 2: res.append(nums[i] + nums[0])
            else: res.append(nums[i] + max(res[i-2], res[i-3]))
        return max(res[-1], res[-2])
        