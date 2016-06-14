# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        while cur is not None and cur.next:
            self.helper(cur)
            cur = cur.next.next
        return dummy.next

    def helper(self, node):
        x, y = node.next, node.next.next
        if y is not None:
            node.next, x.next, y.next = y, y.next, x
