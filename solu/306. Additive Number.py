class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def dfs(num, start, mid, end):
            num1, num2 = num[start:mid], num[mid:end]
            if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'): return False
            num3 = str(int(num1) + int(num2))
            if end+len(num3) > len(num): return False
            if num3 == num[end:end+len(num3)]:
                if end+len(num3) == len(num): return True
                return dfs(num, mid, end, end+len(num3))
            return False

        if len(num)<3: return False
        for i in range(1, len(num)):
            for j in range(i+1, len(num)+1):
                res = dfs(num, 0, i, j)
                if res: return True
        return False