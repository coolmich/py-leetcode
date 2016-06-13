class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y, z = 0, x
        while x:
            y = y*10 + x%10
            x /= 10
        return z==y
