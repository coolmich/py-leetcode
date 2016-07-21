# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        cur = head
        while cur.next and cur.next.next:
            cur = cur.next.next
        pre, post = head, cur
        while pre != post:
            tmp = pre.next
            pre.next, cur.next, tmp.next = tmp.next, tmp, cur.next
            cur, pre = cur.next, pre.next
        return head
