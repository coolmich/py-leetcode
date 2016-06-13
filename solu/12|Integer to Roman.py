class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result, i = [], 0
        while num:
            if num%10:
                result.append(self.helper(num%10, i))
            i += 1
            num /= 10
        return "".join(result[::-1])

    def helper(self, digit, pos):
        ONE = ['I', 'X', 'C', 'M']
        FIVE = ['V', 'L', 'D']
        if digit < 4:
            return ONE[pos]*digit
        elif digit < 5:
            return ONE[pos] + FIVE[pos]
        elif digit < 9:
            return FIVE[pos] + (digit-5)*ONE[pos]
        else:
            return ONE[pos] + [pos+1]
