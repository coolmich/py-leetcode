class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        stack = [1]
        while rowIndex > 0:
            stack = [1] + [stack[i] + stack[i+1] for i in range(len(stack)-1)] + [1]
            rowIndex -= 1
        return stack