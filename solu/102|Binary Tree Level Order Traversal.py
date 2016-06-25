# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        oldStack, res = [root], []
        while len(oldStack):
            tmp, newStack = [], []
            for i in range(len(oldStack)):
                item = oldStack[i]
                tmp.append(item.val)
                if item.left: newStack.append(item.left)
                if item.right: newStack.append(item.right)
            res.append(tmp)
            oldStack = newStack
        return res