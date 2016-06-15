class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len, stack = 0, [-1]
        for idx, item in enumerate(s):
            if item == '(':
                stack.append(idx)
            else:
                if len(stack) > 1:
                    stack.pop()
                    max_len = max(max_len, idx - stack[-1])
                else:
                    stack[0] = idx
        return max_len