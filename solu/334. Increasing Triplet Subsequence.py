class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if not nums: return False
        # mini, runmin1 = 0x7fffffff, []
        # for num in nums:
        #     mini = min(mini, num)
        #     runmin1.append(mini)
        # mini, runmin2 = 0x7fffffff, []
        # for minia, num in zip(runmin1, nums):
        #     if minia == num:
        #         runmin2.append(None)
        #     else:
        #         mini = min(mini, num)
        #         runmin2.append(mini)
        # for mini, num in zip(runmin2, nums):
        #     if mini is not None and num > mini:
        #         return True
        # return False

        min1, min2 = 0x7fffffff, 0x7fffffff
        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True
        return False