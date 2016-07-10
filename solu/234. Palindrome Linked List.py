# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
        while fast.next: fast = fast.next
        while slow != fast and slow.next != fast:
            tmp = slow.next
            slow.next, fast.next, tmp.next = tmp.next, tmp, fast.next
        slow, cur = slow.next, head
        while slow:
            if slow.val != cur.val: return False
            slow, cur = slow.next, cur.next
        return True
