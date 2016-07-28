class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mapi = {}
        # for num in nums:
        #     if num in mapi: continue
        #     if num-1 not in mapi and num+1 not in mapi:
        #         mapi[num] = num
        #     elif num-1 in mapi and num+1 in mapi:
        #         newH, newT = mapi[num-1], mapi[num+1]
        #         mapi[num-1], mapi[num], mapi[num+1] = num-1, num, num+1
        #         mapi[newH], mapi[newT] = newT, newH
        #     elif num-1 in mapi:
        #         newH, mapi[num-1] = mapi[num-1], num-1
        #         mapi[newH], mapi[num] = num, newH
        #     else:
        #         newT, mapi[num+1] = mapi[num+1], num+1
        #         mapi[num], mapi[newT] = newT, num
        # return max([mapi[num] - num for num in nums]) + 1
        for num in nums:
            mapi[num] = num
        maxi = 0
        for num in nums:
            if num-1 not in mapi:
                cur = num
                while cur in mapi: cur += 1
                maxi = max(maxi, cur - num)
        return maxi

            