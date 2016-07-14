class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        while left < len(nums):
            while left < len(nums) and nums[left]: left += 1
            if left == len(nums): return
            right = left
            while right < len(nums) and not nums[right]: right += 1
            if right == len(nums): return
            nums[left], nums[right] = nums[right], nums[left]
