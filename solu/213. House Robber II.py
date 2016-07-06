class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def help(nums):
            if not len(nums): return 0
            if len(nums) < 2: return nums[0]
            res = [nums[0], max(nums[0], nums[1])]
            for idx, num in enumerate(nums[2:]):
                res.append(max(res[-1], num+res[-2]))
            return max(res[-1], res[-2])
        if not len(nums): return 0
        if len(nums) < 2: return nums[0]
        return max(help(nums[:-1]), help(nums[1:]))