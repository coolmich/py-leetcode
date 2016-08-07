# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root: return None
        if not root.left and not root.right: return root.val
        if target == root.val: return root.val
        to_cmp = self.closestValue(root.left, target) if target < root.val else self.closestValue(root.right, target)
        if to_cmp is None: return root.val
        if abs(target-to_cmp) < abs(target-root.val): return to_cmp
        return root.val