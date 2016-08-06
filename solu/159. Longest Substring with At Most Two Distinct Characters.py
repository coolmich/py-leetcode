class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen, mapi, l, maxi = 0, {}, 0, 0
        for idx, item in enumerate(s):
            if item not in mapi:
                if seen < 2: seen += 1
                else:
                    while l < idx:
                        if mapi[s[l]] == l:
                            mapi.pop(s[l])
                            l += 1
                            break
                        l += 1
            mapi[item] = idx
            maxi = max(maxi, idx-l+1)
        return maxi