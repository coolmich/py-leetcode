class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        for num in nums: cur ^= num
        return cur