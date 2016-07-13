# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start <= end:
            mid = (start+end)/2
            if isBadVersion(mid):
                end = mid-1
            else:
                start = mid+1
        if isBadVersion(start): return start
        else: return start - 1
        