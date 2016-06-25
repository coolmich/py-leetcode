# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            if self.isSameTree(p.left, q.left) and p.val == q.val:
                return self.isSameTree(p.right, q.right)
            return False
        elif (p and not q) or (not p and q):
            return False
        else:
            return True