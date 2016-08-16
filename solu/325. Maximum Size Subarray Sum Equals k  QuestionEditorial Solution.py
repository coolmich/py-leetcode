class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cum, wanted, maxi = 0, {}, 0
        wanted[k] = -1
        for idx, num in enumerate(nums):
            cum += num
            if cum in wanted:
                maxi = max(maxi, idx - wanted[cum])
            if cum+k not in wanted:
                wanted[cum+k] = idx
        return maxi