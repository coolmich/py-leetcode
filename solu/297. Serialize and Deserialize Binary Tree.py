# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def helper(node, arr):
            if not node: arr.append('#')
            else:
                arr.append(str(node.val))
                helper(node.left, arr)
                helper(node.right, arr)
        arr = []
        helper(root, arr)
        return ','.join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper(s):
            v = s.pop()
            if v == '#':
                return None
            node = TreeNode(int(v))
            node.left = helper(s)
            node.right = helper(s)
            return node
        return helper(data.split(',')[::-1])

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))