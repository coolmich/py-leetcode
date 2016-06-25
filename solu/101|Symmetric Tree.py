# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.helper(root.left, root.right)

    def helper(self, p, q):
        if p and q:
            if self.helper(p.left, q.right) and p.val == q.val:
                return self.helper(p.right, q.left)
            return False
        elif not p and not q:
            return True
        else:
            return False