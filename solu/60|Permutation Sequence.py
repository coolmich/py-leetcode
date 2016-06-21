import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def helper(nums, k):
            if len(nums) == 1: return nums[0]
            fac = math.factorial(len(nums) - 1)
            idx = k / fac
            return nums[idx] + helper(nums[:idx]+nums[idx+1:], k % fac)

        return helper([str(i) for i in range(1, n+1)], k-1)