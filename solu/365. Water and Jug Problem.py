class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        return x + y == z or ((x + y > z) and z % gcd(x, y) == 0)