# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        stack, res = [root], []
        while len(stack):
            newS = []
            for item in stack:
                if item.left: newS.append(item.left)
                if item.right: newS.append(item.right)
            res.append([item.val for item in stack])
            stack = newS
        return res[::-1]
            