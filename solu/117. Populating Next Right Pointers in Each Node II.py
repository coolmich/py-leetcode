# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        def next_ava(node):
            if not node: return None, None
            if node.left or node.right:
                return (node, node.left) if node.left else (node, node.right)
            return next_ava(node.next)
        if not root: return
        cur = root.right
        if root.left: root.left.next, cur = root.right, root.left
        while cur:
            iter, c = cur, None
            while iter:
                p, n = next_ava(iter)
                if not p: break
                if c: c.next = n
                c = n
                if p.left and p.right: p.left.next = c = p.right
                iter = p.next
            p, n = next_ava(cur)
            cur = n