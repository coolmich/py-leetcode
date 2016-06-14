class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "": return 0
        ipo = self.ipo(needle)
        idx, go = 0, 0
        while idx < len(haystack):
            go = 0
            while idx + go < len(haystack) and go < len(needle) and needle[go] == haystack[idx + go]:
                go += 1
            if go == len(needle):
                return idx
            if idx + go == len(haystack):
                return -1
            if go > 0 and ipo[go-1]:
                idx += (go - ipo[go-1])
            else:
                idx += max(1, go)
        return -1

    def ipo(self, needle):
        ipo = [0] * len(needle)
        track = 0
        for i in range(1, len(needle)):
            if needle[i] != needle[track]:
                track = 0
            if needle[i] == needle[track]:
                ipo[i] = track = track + 1
        return ipo