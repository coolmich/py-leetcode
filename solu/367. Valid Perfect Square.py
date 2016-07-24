class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num/2+1
        while l < r:
            mid = int((l+r)/2)
            if mid**2 == num: return True
            elif mid**2 < num:
                l = mid+1
            else:
                r = mid - 1
        return r**2 == num