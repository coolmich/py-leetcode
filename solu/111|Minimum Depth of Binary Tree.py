# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        stack, i = [root], 1
        while True:
            newS = []
            for item in stack:
                if (not item.left) and (not item.right): return i
                if item.left: newS.append(item.left)
                if item.right: newS.append(item.right)
            stack, i = newS, i+1