import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2: return []
        h, res = [], []
        for i in range(len(nums1)):
            heapq.heappush(h, (nums1[i]+nums2[0], (i, 0)))
        while len(res) < k and len(h):
            _, (i,j) = heapq.heappop(h)
            res.append([nums1[i],nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(h, (nums1[i]+nums2[j+1], (i, j+1)))
        return res