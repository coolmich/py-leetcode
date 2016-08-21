# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap, dummy = [], ListNode(None)
        cur = dummy
        for i in range(len(lists)):
            if lists[i] is not None: heapq.heappush(heap, (lists[i].val, lists[i]))
        while heap:
            val, node = heapq.heappop(heap)
            cur.next = node
            if node.next: heapq.heappush(heap, (node.next.val, node.next))
            cur = cur.next
        return dummy.next