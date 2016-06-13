class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapi = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res = 0
        for idx in range(len(s)):
            if idx > 0 and mapi[s[idx]] > mapi[s[idx-1]]:
                res += (mapi[s[idx]] - 2*mapi[s[idx-1]])
            else:
                res += mapi[s[idx]]
        return res