class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twosum(numi, target):
            l, r = 0, len(numi) - 1
            ret = []
            while l < r:
                res = numi[l] + numi[r]
                if res == target:
                    ret.append((numi[l], numi[r]))
                    l, r = l + 1, r - 1
                    while l+1 < len(numi) and numi[l] == numi[l-1]: l += 1
                    while r-1 >= 0 and numi[r] == numi[r+1]: r -= 1
                elif res < target: l += 1
                else: r -= 1
            return ret
        ret, nums = [], sorted(nums)
        for idx, num in enumerate(nums):
            if idx and num == nums[idx-1]: continue
            for num1, num2 in twosum(nums[idx+1:], -num): ret.append([num, num1, num2])
        return ret
print Solution().threeSum([-1,0,1,2,-1,-4])