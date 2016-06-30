# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        if not fast or not fast.next: return None
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow