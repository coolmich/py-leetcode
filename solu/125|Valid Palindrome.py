class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right, s = 0, len(s) - 1, s.lower()
        while left < right:
            while left < right and not s[left].isalnum(): left += 1
            while right > left and not s[right].isalnum(): right -= 1
            if s[left] != s[right]: return False
            left, right = left+1, right-1
        return True