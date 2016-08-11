# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def pre_order(node, q, target, k):
            if node.left: pre_order(node.left, q, target, k)
            if len(q) == k:
                if abs(target-q[0]) > abs(node.val-target): q.popleft()
                else: return
            q.append(node.val)
            if node.right: pre_order(node.right, q, target, k)
        q = deque()
        pre_order(root, q, target, k)
        return [item for item in q]