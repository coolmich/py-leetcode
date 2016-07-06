class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def help(k, n, nums):
            if not len(nums): return []
            if k == 1:
                if nums[0] <= n <= nums[-1]: return [[n]]
                else: return []
            final = []
            for idx, num in enumerate(nums):
                if num*k < n:
                    res = help(k-1, n-num, nums[idx+1:])
                    for arr in res:
                        arr.append(num)
                    final += res
                else: break
            return final
        if not k or not n or n > 9*k: return []
        return help(k, n, [i for i in range(1, 10)])

print Solution().combinationSum3(3, 15)