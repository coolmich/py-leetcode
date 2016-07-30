class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tree, res = Tree(), []
        for num in nums[::-1]:
            res.append(tree.add(TNode(num)))
        return res[::-1]


class TNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.num = 1


class Tree():
    def __init__(self):
        self.root = None

    def add(self, node):
        res, cur = 0, self.root
        if not cur:
            self.root = node
        else:
            while cur != node:
                cur.num += 1
                if node.val < cur.val:
                    if not cur.left: cur.left = node
                    cur = cur.left
                elif node.val > cur.val:
                    res += (cur.num - 1 - (cur.right.num if cur.right else 0))
                    if not cur.right: cur.right = node
                    cur = cur.right
                else:
                    res += (cur.left.num if cur.left else 0)
                    cur = node
        return res