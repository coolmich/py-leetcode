class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        cs = set([str(i) for i in range(1, 27)])
        ans = [0] * len(s)
        for i in range(len(s)):
            if s[i] in cs:
                ans[i] += (ans[i-1] if i > 0 else 1)
            if i > 0 and s[i-1:i+1] in cs:
                ans[i] += (ans[i-2] if i > 1 else 1)
        return ans[-1]
