class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end-1:
            mid = (start+end)/2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]: return mid
            elif nums[mid] < nums[mid-1]: end = mid
            else: start = mid
        return start if nums[start] > nums[end] else end