class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not len(nums): return []
        if len(nums) == 1: return [nums, []]

        nums, i, res = sorted(nums), 0, []
        while i < len(nums) and nums[i] == nums[0]: i+=1
        for item in self.subsetsWithDup(nums[1:]):
            res.append([nums[0]]+item)
        if i == len(nums):
            res.append([])
        else:
            res += self.subsetsWithDup(nums[i:])
        return res
