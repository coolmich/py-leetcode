# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        fast = slow = head
        while fast and fast.next and fast.next.next: slow, fast = slow.next, fast.next.next
        fast, slow.next = slow.next, None
        lh, rh = self.sortList(head), self.sortList(fast)
        newH = lh if lh.val < rh.val else rh
        smaller, larger = (lh, rh) if lh.val < rh.val else (rh, lh)
        while smaller and larger:
            while smaller.next and smaller.next.val < larger.val: smaller = smaller.next
            if not smaller.next:
                smaller.next = larger
                break
            tmp = larger.next
            larger.next, smaller.next, larger, smaller = smaller.next, larger, tmp, larger
        return newH