# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack, res = [root], []
        while stack:
            newS = []
            res.append(stack[-1].val)
            for item in stack:
                if item.left: newS.append(item.left)
                if item.right: newS.append(item.right)
            stack = newS
        return res