class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not len(s): return []
        cache = []
        for i in range(3):
            if int(s[:i+1]) < 256:
                if i > 0 and s[0] == '0': break
                cache.append(s[:i+1])
        for i in range(3):
            cache = self.helper(s, i, cache)
        return [item for item in cache if len(item) == len(s)+3]

    def helper(self, s, dots, cache):
        res = []
        for item in cache:
            length = len(item) - dots
            for i in range(length, min(length+3, len(s))):
                if int(s[length:i+1]) < 256:
                    if i+1-length > 1 and s[length] == '0': break
                    res.append(item + '.' + s[length:i+1])
        return res

print Solution().restoreIpAddresses('0000')