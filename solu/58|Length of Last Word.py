class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, n = len(s) - 1, 0
        while i >= 0 and s[i] == ' ': i -= 1
        while (i-n)>=0 and s[i-n] != ' ': n += 1
        return n