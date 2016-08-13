# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import defaultdict, deque
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        mini, maxi, mapi, q = 0, 0, defaultdict(list), deque([(root, 0)])
        while q:
            node, idx = q.popleft()
            if idx < mini: mini = idx
            elif idx > maxi: maxi = idx
            mapi[idx].append(node.val)
            if node.left: q.append((node.left, idx-1))
            if node.right: q.append((node.right, idx+1))
        return [mapi[i] for i in range(mini, maxi+1)]
