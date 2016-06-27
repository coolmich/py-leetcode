# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        stack, res = [], []
        self.helper(root, stack, sum, res)
        return res

    def helper(self, node, stack, sum, res):
        if not node: return
        if not node.left and not node.right and node.val == sum:
            res.append(stack+[node.val])
        else:
            stack.append(node.val)
            self.helper(node.left, stack, sum-node.val, res)
            self.helper(node.right, stack, sum-node.val, res)
            stack.pop()