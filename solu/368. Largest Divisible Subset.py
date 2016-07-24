class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        nums, dp, max_i, maxlength = sorted(nums), [(i, 1) for i in range(len(nums))], 0, 1
        for i in range(len(nums)):
            maxi, btt = 1, i
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    bt, leng = dp[j]
                    if leng+1 > maxi: maxi, btt = leng+1, j
            dp[i] = btt, maxi
            if maxi > maxlength: max_i, maxlength = i, maxi
        res, cur = [], max_i
        while dp[cur][0] != cur:
            res.append(nums[cur])
            cur = dp[cur][0]
        res.append(nums[cur])
        return res[::-1]