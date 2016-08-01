# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        cache = []
        def findPre(node):
            cur = node.left
            while cur.right and cur.right != node: cur = cur.right
            return cur
        def visit(node, first, cache):
            ret = None
            if cache:
                n = cache.pop()
                if node.val < n.val:
                    if first:
                        ret = n
                    else:
                        ret = node
            cache.append(node)
            return ret
        cur, first, res = root, True, []
        if not cur: return
        while cur:
            if not cur.left:
                ret = visit(cur, first, cache)
                if ret:
                    res.append(ret)
                    if first: res.append(cur)
                    first = False
                cur = cur.right
            else:
                pre = findPre(cur)
                if not pre.right:
                    pre.right = cur
                    if not cur.left and not first: res.append(cur)
                    cur = cur.left
                else:
                    pre.right = None
                    ret = visit(cur, first, cache)
                    if ret:
                        res.append(ret)
                        if first: res.append(cur)
                        first = False
                    cur = cur.right
        if len(res) == 3: res[1] = res[2]
        res[0].val, res[1].val = res[1].val, res[0].val