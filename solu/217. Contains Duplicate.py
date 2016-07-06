class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mapi = {}
        for num in nums:
            if num in mapi: return True
            mapi[num] = 1
        return False