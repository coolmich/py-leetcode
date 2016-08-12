class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def bsearch(nums, sym):
            start, end = 0, len(nums)-1
            while start < end:
                mid = (start+end)/2
                if nums[mid] == sym: return mid
                elif nums[mid] < sym: start = mid + 1
                else: end = mid - 1
            return start
        if not a:
            stack = [b*i+c for i in nums]
            return stack if b>0 else stack[::-1]
        sym = -b/(2.0*a)
        idx = bsearch(nums, sym)
        if idx < len(nums) and nums[idx] > sym: idx -= 1
        if idx < 0: stack = nums[:]
        elif idx == len(nums): stack = nums[::-1]
        else:
            l, r, stack = idx, idx+1, []
            while l >= 0 and r < len(nums):
                if abs(nums[l]-sym) < abs(nums[r]-sym):
                    stack.append(nums[l])
                    l -= 1
                else:
                    stack.append(nums[r])
                    r += 1
            if l < 0: stack += nums[r:]
            if r == len(nums): stack += nums[:l+1][::-1]
        stack = [a*i**2 + b*i + c for i in stack]
        return stack if a > 0 else stack[::-1]
            