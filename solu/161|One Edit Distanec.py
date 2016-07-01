class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1: return False
        if len(s) == len(t):
            return sum([s[i] != t[i] for i in xrange(len(s))]) == 1
        else:
            sm, lg = (s, t) if len(s) < len(t) else (t, s)
            i = 0
            while i < len(sm) and sm[i] == lg[i]: i += 1
            while i < len(sm) and sm[i] == lg[i+1]: i += 1
            return i == len(sm)