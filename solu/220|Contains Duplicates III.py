from collections import defaultdict
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums:
            return False
        if t < 0 or k < 1:
            return False
        mapi = defaultdict(list)
        for idx, num in enumerate(nums):
            if t > 0:
                buck = num / t
                for ki in range(buck-1, buck+2):
                    for i, n in mapi[ki][::-1]:
                        if (idx - i) <= k:
                            if abs(n - num) <= t:
                                return True
                        else:
                            break
            else:
                buck = num
                for i, n in mapi[num][::-1]:
                    if (idx - i) <= k:
                        if abs(n - num) <= t:
                            return True
                    else:
                        break
            mapi[buck].append((idx, num))
        return False
