# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-2**31)
        dummy.next, cur = head, dummy
        while cur:
            while cur and cur.next and cur.val < cur.next.val: cur = cur.next
            if not cur or not cur.next: return dummy.next
            to_rm, pos = cur.next, dummy
            while pos.next and pos.next.val < to_rm.val: pos = pos.next
            cur.next, to_rm.next, pos.next = to_rm.next, pos.next, to_rm
        return dummy.next
