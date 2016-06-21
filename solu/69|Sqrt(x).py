class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        base, tmp = 0, 1
        while True:
            if base**2 <=x < (base+1)**2:
                return base
            while (base+tmp)**2 <= x:
                tmp <<= 1
            base += (tmp>>1)
            tmp = 1