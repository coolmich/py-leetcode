# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def help(root, k):
            if not root: return 0, root
            l_k, l_node = help(root.left, k)
            if l_k == k:
                return l_k, l_node
            elif l_k == k - 1:
                return k, root
            else:
                r_k, r_node = help(root.right, k - 1 - l_k)
                if r_node:
                    return 1+l_k+r_k, r_node
                else:
                    return l_k+1, root
        _, node = help(root, k)
        return node.val
