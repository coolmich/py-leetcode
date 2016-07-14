class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        elmt, j = 0, 0
        for num in nums: elmt ^= num
        for i in range(32):
            if elmt&(1<<i):
                j = i
                break
        num1 = num2 = 0
        for num in nums:
            if num&(1<<j): num1 ^= num
            else: num2 ^= num
        return [num1, num2]
                