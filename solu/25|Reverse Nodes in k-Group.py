# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        while cur:
            cur = self.helper(cur, k)
        return dummy.next
    def helper(self, node, k):
        cnt = k
        cur = node
        while cnt:
            cur = cur.next
            if cur is None:
                return None
            cnt -= 1
        cnt = k - 1
        cur = node.next
        while cnt:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = node.next
            node.next = tmp
            cnt -= 1
        return cur