class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for idx, i in enumerate(nums):
            while idx + 1 != i and 0<=i-1<len(nums):
                if nums[i-1] == nums[idx]: break
                nums[i-1], nums[idx] = nums[idx], nums[i-1]
                i = nums[idx]
        for idx, i in enumerate(nums):
            if idx + 1 != i:
                return idx+1
        return len(nums)+1