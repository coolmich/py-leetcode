# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next, cur, i = head, dummy, 1
        while i < m:
            cur, i = cur.next, i + 1
        back = cur.next
        while i < n:
            tmp = back.next
            back.next, tmp.next, cur.next, i = tmp.next, cur.next, tmp, i+1
        return dummy.next
