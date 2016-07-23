class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        li, s = set(["a","e","o","u","i","A","E","O","U","I"]), list(s)
        left, right = 0, len(s)-1
        while left < right:
            while left < right and s[left] not in li: left += 1
            while right > left and s[right] not in li: right -= 1
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return "".join(s)