# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
    def helper(self, inorder, startI, endI, postorder, startP, endP):
        if startI > endI: return None
        if startI == endI: return TreeNode(inorder[startI])
        root = TreeNode(postorder[endP])
        i = inorder.index(root.val)
        root.left = self.helper(inorder, startI, i-1, postorder, startP, startP + i - 1 - startI)
        root.right = self.helper(inorder, i+1, endI, postorder, startP+i-startI, endP-1)
        return root
