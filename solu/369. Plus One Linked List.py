# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(node):
            to_add = 1 if not node.next else helper(node.next)
            new_val = node.val + to_add
            if new_val > 9:
                node.val = 0
                return 1
            node.val = new_val
            return 0
        ret = helper(head)
        if ret:
            newH = ListNode(1)
            newH.next = head
            return newH
        else:
            return head
        # cur, num = head, 0
        # while cur:
        #     num, cur = num*10 + cur.val, cur.next
        # num, cur = list(str(num+1)), head
        # for i in range(len(num)):
        #     if not cur.next and i < len(num)-1:
        #         cur.next = ListNode(0)
        #     cur.val, cur = int(num[i]), cur.next
        # return head
        