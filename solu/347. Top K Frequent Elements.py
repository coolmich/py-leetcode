from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt, revcnt, res = defaultdict(int), defaultdict(list), []
        for num in nums: cnt[num] += 1
        for num in cnt: revcnt[cnt[num]].append(num)
        for i in range(len(nums), -1, -1):
            if i in revcnt:
                res += revcnt[i]
                if len(res) >= k: break
        return res[:k]