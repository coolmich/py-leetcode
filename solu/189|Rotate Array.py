class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def rev(nums, start, end):
            while start < end:
                nums[start], nums[end], start, end = nums[end], nums[start], start+1, end-1
        k %= len(nums)
        rev(nums, 0, len(nums) - 1)
        rev(nums, 0, k-1)
        rev(nums, k, len(nums)-1)