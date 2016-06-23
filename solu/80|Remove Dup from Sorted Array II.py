class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2: return len(nums)
        fast, slow = 2, 2
        while fast < len(nums):
            nums[slow] = nums[fast]
            if nums[slow] == nums[slow-1] and nums[slow-1] == nums[slow-2]:
                while fast < len(nums) and nums[fast] == nums[slow]: fast += 1
                if fast == len(nums): return slow
                nums[slow] = nums[fast]
            slow, fast = slow+1, fast+1
        return slow