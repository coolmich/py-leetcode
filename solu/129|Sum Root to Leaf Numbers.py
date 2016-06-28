# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, above):
            calc = above*10 + node.val
            if not node.left and not node.right:
                return calc
            num = 0
            if node.left:
                num += helper(node.left, calc)
            if node.right:
                num += helper(node.right, calc)
            return num
        if not root: return 0
        return helper(root, 0)

