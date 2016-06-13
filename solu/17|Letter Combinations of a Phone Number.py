class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        mapi = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = ['']
        for digit in digits:
            res = self.helper(digit, mapi, res)
        return res
    def helper(self, digit, mapi, res):
        return [s+l for l in mapi[digit] for s in res]