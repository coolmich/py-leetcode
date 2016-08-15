# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(node, mapi):
            if node is None: return 0
            lh, rh = helper(node.left, mapi), helper(node.right, mapi)
            h = max(lh, rh) + 1
            mapi[h].append(node.val)
            return h
        mapi = defaultdict(list)
        helper(root, mapi)
        i, res = 1, []
        while i in mapi:
            res.append(mapi[i])
            i += 1
        return res