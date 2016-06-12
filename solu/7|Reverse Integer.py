class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg, x = x < 0, abs(x)
        new_num = int(str(x)[::-1]) * (-1 if neg else 1)
        # new_num = 0
        # neg, x = x < 0, abs(x)
        # while x:
        #     new_num = new_num*10 + x%10
        #     x /= 10
        # new_num = new_num * -1 if neg else new_num
        return new_num if (-(1<<31) <= new_num <= (1<<31) - 1) else 0