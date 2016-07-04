class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        def rev(s, start, end):
            while start < end:
                s[start], s[end], start, end = s[end], s[start], start + 1, end - 1
        start = 0
        for idx, item in enumerate(s):
            if item == ' ':
                rev(s, start, idx-1)
                start = idx + 1
        rev(s, start, len(s)-1)
        rev(s, 0, len(s)-1)