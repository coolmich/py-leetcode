# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return res[::-1]