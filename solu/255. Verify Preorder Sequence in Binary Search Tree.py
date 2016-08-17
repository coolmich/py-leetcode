class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # def helper(preorder, start, end):
        #     if start >= end: return True
        #     h, i = preorder[start], start + 1
        #     while i <= end:
        #         if preorder[i] > h: break
        #         i += 1
        #     j = i
        #     while i <= end:
        #         if preorder[i] <= h: return False
        #         i += 1
        #     if not helper(preorder, start+1, j-1): return False
        #     return helper(preorder, j, end)
        # return helper(preorder, 0, len(preorder)-1)
        stack, mini = [], -2**31
        for num in preorder:
            if num < mini: return False
            while stack and num > stack[-1]:
                mini = stack.pop()
            stack.append(num)
        return True