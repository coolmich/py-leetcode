class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start < end:
            if nums[start] < nums[end]: return nums[start]
            if start == end - 1: return min(nums[start], nums[end])
            mid = (start+end)/2
            if nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]: return nums[mid]
            if nums[mid] < nums[start]: end = mid-1
            else: start = mid+1
        return nums[start]