import functools
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        li = []
        for num in nums:
            if not li or num > li[-1]:
                li.append(num)
            else:
                low, high = 0, len(li)
                while low < high:
                    mid = (low+high)/2
                    if li[mid] == num:
                        low = high = mid
                    elif li[mid] < num:
                        low = mid+1
                    else:
                        high = mid
                li[high] = num
        return len(li)

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def comparator(x, y):
            if x[0] < y[0]: return -1
            elif x[0] > y[0]: return 1
            else:
                if x[1] > y[1]: return -1
                elif x[1] < y[1]: return 1
                else: return 0
        li = [i[1] for i in sorted(envelopes, key=functools.cmp_to_key(comparator))]
        return self.lengthOfLIS(li)
        