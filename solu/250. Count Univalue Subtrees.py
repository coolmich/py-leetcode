# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def check(node, maxi):
            if node is None: return 0
            if not node.left and not node.right: return 1
            l, r = check(node.left, maxi), check(node.right, maxi)
            if l < 0 or r < 0: return -1
            if (node.left and node.left.val != node.val) or (node.right and node.right.val != node.val): return -1
            ret = l + r + 1
            maxi[0] = max(maxi[0], ret)
            return ret
        if root is None: return 0
        maxi = [1]
        check(root, maxi)
        return maxi[0]

node1 = TreeNode(5)
node2 = TreeNode(5)
node3 = TreeNode(5)
node4 = TreeNode(5)
node5 = TreeNode(1)
node5.left = node1
node5.right = node2
node2.left = node3
node2.right = node4
print Solution().countUnivalSubtrees(node5)