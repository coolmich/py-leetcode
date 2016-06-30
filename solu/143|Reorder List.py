# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        fast = head
        while fast and fast.next != slow: fast = fast.next
        fast.next = None
        h = self.reverse_list(slow)
        cur = head
        while cur:
            tmp = h.next
            h.next, cur.next, h, cur = cur.next, h, tmp, cur.next
        if h:
            cur = head
            while cur.next: cur = cur.next
            cur.next = h
    def reverse_list(self, node):
        dummy = ListNode(None)
        dummy.next = node
        while node.next:
            mv = node.next
            node.next, mv.next, dummy.next = mv.next, dummy.next, mv
        return dummy.next