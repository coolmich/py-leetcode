# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k: return head
        dummy = ListNode(None)
        dummy.next = head
        cur, cnt = dummy, k
        while cnt > 0 and cur:
            cur, cnt = cur.next, cnt-1
        if not cur:
            k %= (k-cnt-1)
            if not k: return head
            cur = dummy
            while k > 0:
                cur, k = cur.next, k-1
        slow = dummy
        if not cur.next:
            return head
        while cur.next:
            slow, cur = slow.next, cur.next
        dummy.next = slow.next
        cur.next = head
        slow.next = None
        return dummy.next