class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        neg = (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        num, rem, mapi, frac = str(numerator / denominator), numerator % denominator, {}, []
        while rem:
            if rem in mapi: break
            mapi[rem] = len(mapi)
            rem *= 10
            frac.append(str(rem / denominator))
            rem %= denominator
        if not len(frac):
            return ('-' if neg else '') + str(num)
        if rem:
            frac = ''.join(frac[:mapi[rem]]) + '(' + ''.join(frac[mapi[rem]:]) + ')'
        else:
            frac = ''.join(frac)
        return ('-' if neg else '') + num + '.' + frac