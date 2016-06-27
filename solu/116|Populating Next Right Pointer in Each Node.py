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
        mostleft = root
        while mostleft:
            cur = mostleft
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                else: return
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            mostleft = mostleft.left
            