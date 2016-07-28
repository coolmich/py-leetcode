import math
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def calc(stack, li, limit):
            for num in li:
                for i in range(limit):
                    if num & (1<<i): stack[31-i] += 1
        expect, real, num, limit = [0]*32, [0]*32, 0, min(32, int(math.log(len(nums), 2)) + 1)
        calc(expect, range(len(nums)), limit)
        calc(real, nums, limit)
        for i in range(limit):
            if expect[31-i] < real[31-i]:
                num |= (1<<i)
        return num

print Solution().findDuplicate([14,16,12,1,16,17,6,8,5,19,16,13,16,3,11,16,4,16,9,7])