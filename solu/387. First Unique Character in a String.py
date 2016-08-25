from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(list(s))
        for idx, l in enumerate(s):
            if c[l] == 1: return idx
        return -1