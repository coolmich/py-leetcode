# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        slow, fast = dummy, head
        while fast:
            if (fast.next and fast.val != fast.next.val) or not fast.next:
                slow, fast = slow.next, fast.next
            else:
                while fast.next and fast.val == fast.next.val: fast = fast.next
                slow.next = fast = fast.next
        return dummy.next
