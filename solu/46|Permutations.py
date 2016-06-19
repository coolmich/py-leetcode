class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        res = []
        for idx, item in enumerate(nums):
            for perm in self.permute(nums[:idx] + nums[idx+1:]):
                perm.append(item)
                res.append(perm)
        return res