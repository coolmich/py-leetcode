class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        num1 = list(reversed(num1))
        num2 = list(reversed(num2))
        for i in range(len(num1)):
            carryM = 0
            carryA = 0
            for j in range(len(num2)):
                prod = int(num2[j]) * int(num1[i]) + carryM
                carryM = prod / 10
                sumi = res[j+i] + prod%10 + carryA
                res[i+j] = sumi%10
                carryA = sumi / 10
            while carryM or carryA:
                sumi = carryM + carryA + res[i+len(num2)]
                res[i+len(num2)] = sumi % 10
                carryM, carryA = 0, sumi/10
        for i in range(len(res)-1, -1, -1):
            if res[i] != 0: break
        return "".join(list(reversed([str(x) for x in res[:i+1]])))
