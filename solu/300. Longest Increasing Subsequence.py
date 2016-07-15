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