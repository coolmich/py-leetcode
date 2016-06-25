# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def pp(self):
        print self.val
        if self.left: self.left.pp()
        if self.right: self.right.pp()

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n: return []
        mapi = {}
        li = list(range(1, n+1))
        self.helper(li, mapi)
        return mapi[(li[0], li[-1])]
    def helper(self, li, mapi):
        if not len(li): return [None]
        k = (li[0], li[-1])
        if k not in mapi:
            if len(li) == 1:
                mapi[k] = [TreeNode(li[0])]
            else:
                res = []
                for i in range(len(li)):
                    leftRes = self.helper(li[:i], mapi)
                    rightRes = self.helper(li[i+1:], mapi)
                    for l in leftRes:
                        for r in rightRes:
                            root = TreeNode(li[i])
                            root.left = l
                            root.right = r
                            res.append(root)
                mapi[k] = res
        return mapi[k]

print Solution().generateTrees(3)