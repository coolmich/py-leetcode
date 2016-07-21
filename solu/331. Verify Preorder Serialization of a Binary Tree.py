class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        def helper(preorder, start):
            if len(preorder) <= start: return -1
            if preorder[start] == '#': return start+1
            l = helper(preorder, start+1)
            if len(preorder) == l or l == -1: return -1
            r = helper(preorder, l)
            return r
        preorder = preorder.split(',')
        return helper(preorder, 0) == len(preorder)
