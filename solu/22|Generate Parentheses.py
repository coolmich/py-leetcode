class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']
        result = []
        for left in range(n):
            leftres = self.generateParenthesis(left)
            rightres = self.generateParenthesis(n-1-left)
            result += ['('+l+')'+r for l in leftres for r in rightres]
        return result