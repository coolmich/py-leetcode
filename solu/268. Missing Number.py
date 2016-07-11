class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (1+len(nums))*len(nums)/2 - sum(nums)