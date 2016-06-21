class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            new_digit = digits[i] + carry
            if new_digit == 10:
                carry, digits[i] = 1, 0
            else:
                carry, digits[i] = 0, new_digit
                break
        if carry:
            return [1] + digits
        else:
            return digits