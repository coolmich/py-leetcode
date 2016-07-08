class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def help(lower, upper):
            if lower == upper: return str(lower)
            return '{}->{}'.format(lower, upper)
        if not nums: return []
        res, lower, cnt = [], nums[0], 0
        for idx, num in enumerate(nums):
            if num != lower + cnt:
                res.append(help(lower, lower+cnt-1))
                lower, cnt = num, 1
            else:
                cnt += 1
        res.append(help(lower, lower+cnt-1))
        return res