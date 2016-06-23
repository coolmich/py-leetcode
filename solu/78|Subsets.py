class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1: return [nums, []]
        res = []
        arr = self.subsets(nums[1:])
        if arr:
            for li in arr:
                res.append(li)
                res.append(li+[nums[0]])
        return res
