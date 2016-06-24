class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        a, b = m-1, n-1
        for i in range(m+n-1, -1, -1):
            if a >= 0 and b >= 0:
                if nums1[a] < nums2[b]:
                    nums1[i], b = nums2[b], b-1
                else:
                    nums1[i], a = nums1[a], a-1
            elif a >= 0: break
            else:
                nums1[i], b = nums2[b], b-1
