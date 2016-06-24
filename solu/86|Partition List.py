# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        left = dummy
        while left.next and left.next.val < x: left = left.next
        right = left
        while right:
            while right.next and right.next.val >= x: right = right.next
            if not right.next: break
            tmp = right.next
            right.next, tmp.next, left.next, left = tmp.next, left.next, tmp, tmp
        return dummy.next