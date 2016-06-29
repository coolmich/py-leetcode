class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [0] * 32
        for num in nums:
            cur = 1
            for i in range(32):
                bits[31-i] += (num >> i) & cur
        cur, neg = 0, bits[0] %3
        if bits[0] % 3:
            for i in range(32):
                bits[i] = 1-bits[i]%3
        for i in range(32):
            cur = cur | ((bits[i]%3) << (31-i))
        if neg:
            cur = -1 * (cur+1)
        return cur

