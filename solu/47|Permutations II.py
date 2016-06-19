class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums):
            if len(nums) == 0: return []
            if len(nums) == 1: return [nums]
            res = []
            for idx, item in enumerate(nums):
                if idx == 0 or (idx > 0 and nums[idx-1] != item):
                    for perm in helper(nums[:idx] + nums[idx+1:]):
                        perm.append(item)
                        res.append(perm)
            return res
        return helper(sorted(nums))