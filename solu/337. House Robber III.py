# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # def max_rob(node, cache):
        #     if not node: return 0
        #     if node in cache: return cache[node]
        #     n1, n2 = 0, 0
        #     if node.left:
        #         n1 += max_rob(node.left, cache)
        #         n2 += (max_rob(node.left.left, cache) + max_rob(node.left.right, cache))
        #     if node.right:
        #         n1 += max_rob(node.right, cache)
        #         n2 += (max_rob(node.right.left, cache) + max_rob(node.right.right, cache))
        #     res = max(node.val+n2, n1)
        #     cache[node] = res
        #     return res
        # cache = {}
        # return max_rob(root, cache)

        def max_rob(node):
            if not node: return (0, 0)
            if not node.left and not node.right: return (node.val, 0)
            (l1, l2), (r1, r2) = max_rob(node.left), max_rob(node.right)
            return (l2+r2+node.val, max(l1, l2)+max(r1,r2))
        return max(max_rob(root))