class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        res = ''.join(self.mergeS(nums))
        i = 0
        while i < len(res) and res[i] == '0': i += 1
        if i == len(res): return '0'
        return res[i:]

    def mergeS(self, nums):
        def compare(num1, num2):
            if len(num1) == len(num2):
                return num1 > num2
            else:
                return (num1 + num2) > (num2 + num1)
        if len(nums) < 2: return nums
        mid = len(nums) / 2
        l1, l2 = self.mergeS(nums[:mid]), self.mergeS(nums[mid:])
        res, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if compare(l1[i], l2[j]):
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        res += (l1[i:] + l2[j:])
        return res
        