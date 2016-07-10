from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapi = defaultdict(int)
        for l in s: mapi[l] += 1
        for l in t:
            mapi[l] -= 1
            if mapi[l] < 0: return False
        return sum(mapi.values()) == 0