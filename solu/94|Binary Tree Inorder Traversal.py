# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack, li = [], []
        cur = root
        while cur:
            stack.append(cur)
            cur = cur.left
        while stack:
            node = stack.pop()
            li.append(node.val)
            if node.right:
                cur = node.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
        return li