import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # heap = []
        # for num in nums:
        #     if len(heap) < k:
        #         heapq.heappush(heap, num)
        #     else:
        #         heapq.heappushpop(heap, num)
        # return heap[0]
        def select_sort(s, e):
            l, r = s, e - 1
            while l < r:
                while l < r and nums[l] < nums[e]: l += 1
                while l < r and nums[r] >= nums[e]: r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            nums[l], nums[e] = nums[e], nums[l]
            return l
        s, e = 0, len(nums)-1
        i, k = select_sort(s, e), len(nums)-k
        print i
        print nums
        while i != k:
            # print '{},{}'.format(i, k)
            if i < k: s = i + 1
            else: e = i - 1
            i = select_sort(s, e)
        return nums[i]
print Solution().findKthLargest([3,2,1,1,5,5, 5, 6,4], 2)