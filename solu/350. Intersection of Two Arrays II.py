from collections import defaultdict
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mapi, res = defaultdict(int), []
        for num in nums1:
            mapi[num] += 1
        for num in nums2:
            if num in mapi and mapi[num] > 0:
                res.append(num)
                mapi[num] -= 1
        return res