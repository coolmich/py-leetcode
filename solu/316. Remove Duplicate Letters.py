from collections import Counter
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = Counter(list(s))
        stack = []
        for l in s:
            if l not in stack:
                while stack and l < stack[-1] and c[stack[-1]] > 0:
                    n = stack.pop()
                    # c[n] -= 1
                stack.append(l)
            c[l] -= 1
        return ''.join(stack)

