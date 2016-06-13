class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for item in s:
            if item in ('(', '{', '['):
                stack.append(item)
            else:
                if len(stack) > 0 and ((item == ')' and stack[-1] == '(') or (item == '}' and stack[-1] == '{') or (item == ']' and stack[-1] == '[')):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0