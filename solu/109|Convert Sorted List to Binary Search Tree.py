# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        i, cur = 0, head
        while cur: cur, i = cur.next, i+1
        root, _ = self.helper(head, i)
        return root

    def helper(self, head, num):
        if not head or num == 0: return None, head
        if num == 1: return TreeNode(head.val), head.next
        mid = num/2
        left, nn = self.helper(head, mid)
        root = TreeNode(nn.val)
        right, nnn = self.helper(nn.next, num - mid - 1)
        root.left, root.right = left, right
        return root, nnn