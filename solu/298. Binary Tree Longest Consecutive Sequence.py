# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, maxi):
            if not root: return 0
            l = helper(root.left, maxi)
            r = helper(root.right, maxi)
            if root.left and not root.left.val - 1 == root.val: l = 0
            if root.right and not root.right.val - 1 == root.val: r = 0
            res = max(l, r) + 1
            if res > maxi[0]: maxi[0] = res
            return res
        arr = [0]
        helper(root, arr)
        return arr[0]