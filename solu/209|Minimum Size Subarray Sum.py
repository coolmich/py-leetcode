class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums): return 0
        left = right = 0
        minL, sumi = 2**31, nums[0]
        while right < len(nums) - 1:
            while right < len(nums)-1 and sumi < s:
                right += 1
                sumi += nums[right]
            if sumi >= s:
                minL = min(minL, right - left + 1)
                while left <= right and sumi >= s:
                    sumi, left = sumi - nums[left], left + 1
                # left -= 1
                # if left == right: return 1
                if sumi < s:
                    minL = min(minL, right - left + 2)
        return minL if minL != 2**31 else 0

print Solution().minSubArrayLen(3, [1,1])