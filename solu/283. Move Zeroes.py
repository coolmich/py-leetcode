class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j], j = nums[i], j + 1
        while j < len(nums): nums[j], j = 0, j + 1