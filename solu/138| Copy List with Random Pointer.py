# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return head
        mapi = {}
        cur = head
        while cur:
            if cur not in mapi: mapi[cur] = RandomListNode(cur.label)
            cur = cur.next
        cur = head
        while cur:
            if cur.next: mapi[cur].next = mapi[cur.next]
            if cur.random: mapi[cur].random = mapi[cur.random]
            cur = cur.next
        return mapi[head]
