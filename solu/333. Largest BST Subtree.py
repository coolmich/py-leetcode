# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import OrderedDict
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def check(node, maxi):
            if not node.left and not node.right: return 1, node.val, node.val
            l = r = 0
            lmin = rmax = node.val
            invalid = False
            if node.left:
                l, lmin, lmax = check(node.left, maxi)
                if l == -1 or lmin >= node.val or lmax >= node.val: invalid = True
            if node.right:
                r, rmin, rmax = check(node.right, maxi)
                if r == -1 or rmin <= node.val or rmax <= node.val: invalid = True
            if invalid: return -1, -1, -1
            ret = l + r + 1
            maxi[0] = max(maxi[0], ret)
            return ret, lmin, rmax
        if root is None: return 0
        maxi = [1]
        check(root, maxi)
        return maxi[0]