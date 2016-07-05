# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        dummy = ListNode(None)
        dummy.next, cur = head, dummy
        while cur.next: cur = cur.next
        while dummy.next != cur:
            tmp = dummy.next
            dummy.next, tmp.next, cur.next = tmp.next, cur.next, tmp
        return dummy.next