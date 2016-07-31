from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q, res = deque(), []
        for i in range(k):
            while q and nums[q[-1]] < nums[i]: q.pop()
            q.append(i)
        if q: res.append(nums[q[0]])
        for i in range(k, len(nums)):
            if q and q[0] <= i-k: q.popleft()
            while q and nums[q[-1]] < nums[i]: q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res
