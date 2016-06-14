class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = -1 if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor or dividend == 0:
            return 0
        if dividend == divisor:
            return neg * 1
        bigger = divisor
        res = 1
        while bigger < dividend:
            bigger <<= 1
            res <<= 1
        result = neg * ((res>>1) + self.divide(dividend - (bigger>>1), divisor))
        return min(2147483647, max(-2147483648, result))