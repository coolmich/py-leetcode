# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        cur = p.right
        if cur is not None:
            while cur.left: cur = cur.left
            return cur
        cur, maxi = root, None
        while cur != p:
            if p.val < cur.val:
                cur, maxi = cur.left, cur.val
            else: cur = cur.right
        return maxi