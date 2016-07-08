# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # def help(node):
        #     if not node: return 0, 0
        #     if not node.left and not node.right:
        #         return 1, 1
        #     else:
        #         lv, idx = help(node.left)
        #         if idx < 2**(lv-1):
        #             return lv+1, idx
        #         else:
        #             rv, ridx = help(node.right)
        #             if rv < lv:
        #                 return lv+1, idx
        #             else:
        #                 return lv+1, idx+ridx
        # lv, idx = help(root)
        # if not lv: return 0
        # return (2**(lv - 1) - 1)+idx
        if not root: return 0
        l, r, cntl, cntr = root.left, root.right, 0, 0
        while l: l, cntl = l.left, cntl+1
        while r: r, cntr = r.right, cntr+1
        if cntl != cntr:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
        return 2**(cntl+1) - 1