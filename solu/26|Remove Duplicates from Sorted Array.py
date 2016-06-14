class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = 0, 0
        while fast < len(nums):
            val = nums[fast]
            while fast < len(nums) and nums[fast] == val:
                fast += 1
            nums[slow] = val
            slow += 1
        return slow