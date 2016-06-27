# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0: return None
        return self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
    def helper(self, preorder, startP, endP, inorder, startI, endI):
        if startP == endP: return TreeNode(preorder[startP])
        if startP > endP: return None
        root = TreeNode(preorder[startP])
        index = inorder.index(root.val)
        root.left = self.helper(preorder, startP+1, startP+index-startI, inorder, startI, index-1)
        root.right = self.helper(preorder, startP+index-startI+1, endP, inorder, index+1, endI)
        return root