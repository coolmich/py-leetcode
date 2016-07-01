# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA, curB, cntA, cntB = headA, headB, 0, 0
        while curA: curA, cntA = curA.next, cntA+1
        while curB: curB, cntB = curB.next, cntB+1
        curA, curB = headA, headB
        while curA and cntA > cntB:
            curA, cntA = curA.next, cntA - 1
        while curB and cntB > cntA:
            curB, cntB = curB.next, cntB - 1
        while curA and curB and curA != curB:
            curA, curB = curA.next, curB.next
        return curA

# this is better: http://www.cnblogs.com/yuzhangcmu/p/4128794.html