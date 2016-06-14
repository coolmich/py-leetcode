class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) >= 2:
            for idx in range(len(nums)-1, 0, -1):
                if nums[idx] > nums[idx-1]:
                    for i in range(len(nums)-1, idx-1, -1):
                        if nums[i] > nums[idx-1]:
                            nums[i], nums[idx-1] = nums[idx-1], nums[i]
                            break
                    nums[idx:] = reversed(nums[idx:])
                    return
            nums[:] = reversed(nums[:])