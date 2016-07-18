class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.original = nums[:]
        self.arr = nums[:]
        for i in range(1, len(nums)+1):
            lb, idx = self.lowbit(i), i-2
            while idx > i-1-lb:
                self.arr[i-1] += self.arr[idx]
                idx -= self.lowbit(idx+1)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        to_add, idx = val - self.original[i], i
        while i < len(self.arr):
            self.arr[i] += to_add
            i += self.lowbit(i+1)
        self.original[idx] = val


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        while j >= i:
            res += self.arr[j]
            j -= self.lowbit(j+1)
        i -= 1
        while i > j:
            res -= self.arr[i]
            i -= self.lowbit(i+1)
        return res

    def lowbit(self, num):
        return num & (-num)
