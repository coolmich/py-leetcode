class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end)/2
            if target == nums[mid]:
                break
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        if start > end:
            return [-1, -1]
        while mid >= 0 and nums[mid] == target:
            mid -= 1
        result, mid = [mid+1], mid+1
        while mid < len(nums) and nums[mid] == target:
            mid += 1
        result.append(mid-1)
        return result
