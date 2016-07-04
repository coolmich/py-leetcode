class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = [ord(item) - 64 for item in s]
        ans, res = 0, res[::-1]
        for i in range(len(res)):
            ans += res[i]*26**i
        return ans
        