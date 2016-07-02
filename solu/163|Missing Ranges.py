class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def helper(lower, upper):
            if lower == upper:
                return str(lower)
            else:
                return '{}->{}'.format(lower, upper)
        if not len(nums): return [helper(lower, upper)]
        res = []
        if nums[0] > lower: res.append(helper(lower, nums[0]-1))
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i-1] + 1: res.append(helper(nums[i-1]+1, nums[i]-1))
        if upper > nums[-1]: res.append(helper(nums[-1]+1, upper))
        return res