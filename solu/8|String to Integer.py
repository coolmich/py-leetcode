class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ss = str.strip()
        neg = False
        if len(str) == 0: return 0
        if ss[0] in ('+', '-'):
            neg = True if ss[0] == '-' else False
            ss = ss[1:]
        i = 0
        while i < len(ss):
            if not ss[i].isdigit():
                break
            i += 1
        if i == 0:
            return 0
        num = int(ss[:i]) * (-1 if neg else 1)
        if num < -(1<<31):
            return -(1<<31)
        if num > ((1<<31)-1):
            return ((1<<31)-1)
        return num