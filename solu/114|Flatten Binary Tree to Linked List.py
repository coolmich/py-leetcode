# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        h, t = self.helper(root)

    def helper(self, root):
        if not root: return None, None
        cur = pre = tail = root
        lh, lt = self.helper(root.left)
        rh, rt = self.helper(root.right)
        if lh:
            cur.left = None
            cur.right, cur, tail = lh, lt, lt
        if rh:
            cur.left = None
            cur.right, tail = rh, rt
        return pre, tail
        