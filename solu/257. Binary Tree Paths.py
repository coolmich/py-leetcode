# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def helper(root):
            if not root: return []
            if not root.left and not root.right: return [[str(root.val)]]
            res = []
            for l in (helper(root.left) + helper(root.right)):
                l.append(str(root.val))
                res.append(l)
            return res
        return ['->'.join(li[::-1]) for li in helper(root)]