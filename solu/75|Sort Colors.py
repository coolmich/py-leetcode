class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums) - 1
        while start < len(nums) and nums[start] == 0: start += 1
        while end >= 0 and nums[end] == 2: end -= 1
        if start == len(nums) or end == 0: return
        cur = start
        while cur <= end:
            if nums[cur] == 0:
                nums[cur], nums[start] = nums[start], nums[cur]
                while start <= end and nums[start] == 0: start += 1
                cur = start
            elif nums[cur] == 2:
                nums[cur], nums[end] = nums[end], nums[cur]
                while start <= end and nums[end] == 2: end -= 1
            else:
                cur += 1

