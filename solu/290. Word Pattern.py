class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str, mapi1, mapi2 = str.split(), {}, {}
        if len(str) != len(pattern): return False
        for i in range(len(pattern)):
            if pattern[i] not in mapi1 and str[i] not in mapi2:
                mapi1[pattern[i]] = str[i]
                mapi2[str[i]] = pattern[i]
            elif (pattern[i] in mapi1 and mapi1[pattern[i]] != str[i]) or (str[i] in mapi2 and mapi2[str[i]] != pattern[i]):
                return False
        return True