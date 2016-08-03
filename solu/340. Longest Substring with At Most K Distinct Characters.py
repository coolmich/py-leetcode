class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not k: return 0
        start, mapi, seen, maxi = 0, {}, 0, 0
        for idx, l in enumerate(s):
            if l not in mapi:
                if seen < k:
                    seen += 1
                else:
                    i = start
                    while i < idx:
                        if mapi[s[i]] == i:
                            mapi.pop(s[i])
                            break
                        i += 1
                    start = i+1
            maxi = max(maxi, idx-start+1)
            mapi[l] = idx
        return maxi
