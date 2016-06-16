class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end - 1:
            mid = (start+end)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if target <= nums[start]:
            return start
        elif target <= nums[end]:
            return end
        else:
            return end + 1