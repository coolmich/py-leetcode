class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        sing = (len(nums1) + len(nums2)) % 2
        # first corner case
        if len(nums1) == 0 or len(nums2) == 0:
            return self.helper(nums1 if len(nums1) else nums2, None, sing)
        # when looking for two numbers, target the first one
        rank = (len(nums1) + len(nums2) - 1)/2
        while rank > 0:
            idx = (rank-1)/2
            idx1 = min(idx, len(nums1) - 1)
            idx2 = min(idx, len(nums2) - 1)
            if nums1[idx1] < nums2[idx2]:
                nums1 = nums1[idx1+1:]
                idx = idx1
            else:
                nums2 = nums2[idx2+1:]
                idx = idx2
            rank -= (idx + 1)
            if len(nums1) == 0 or len(nums2) == 0:
                return self.helper(nums1 if len(nums1) else nums2, rank, sing)
        if sing:
            return min(nums1[0], nums2[0])
        else:
            smaller, larger = (nums1, nums2) if nums1[0] < nums2[0] else (nums2, nums1)
            if len(smaller) < 2:
                return (smaller[0] + larger[0]) / 2.0
            else:
                return (smaller[0] + min(larger[0], smaller[1])) / 2.0

    def helper(self, li, pos, sing):
        pos = pos if pos is not None else (len(li)-1)/2
        if sing:
            return li[pos]
        else:
            return (li[pos] + li[pos+1])/2.0
