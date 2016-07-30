class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        known_sum, i, res = 1, 0, 0
        while known_sum <= n:
            if i < len(nums) and nums[i] <= known_sum:
                known_sum += nums[i]
                i += 1
            else:
                res += 1
                known_sum *= 2
        return res
        