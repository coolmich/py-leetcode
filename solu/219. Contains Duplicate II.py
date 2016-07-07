class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapi = {}
        for idx, num in enumerate(nums):
            if num in mapi and (idx - mapi[num]) <= k:
                return True
            mapi[num] = idx
        return False