from collections import defaultdict
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapi = defaultdict(int)
        for l in s:
            if mapi[l]: mapi[l] = 0
            else: mapi[l] = 1
        return sum(mapi.values()) < 2