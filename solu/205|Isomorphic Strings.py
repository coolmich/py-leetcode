class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapi1, mapi2 = {}, {}
        for i in range(len(s)):
            l1, l2 = s[i], t[i]
            if l1 in mapi1:
                if mapi1[l1] != l2 or l2 not in mapi2 or mapi2[l2] != l1:
                    return False
            else:
                if l2 in mapi2:
                    return False
                mapi1[l1], mapi2[l2] = l2, l1
        return True
        