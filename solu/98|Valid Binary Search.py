# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        li = []
        self.helper(root, li)
        for i in range(1, len(li)):
            if li[i] <= li[i-1]: return False
        return True

    def helper(self, node, li):
        if node.left: self.helper(node.left, li)
        li.append(node.val)
        if node.right: self.helper(node.right, li)
