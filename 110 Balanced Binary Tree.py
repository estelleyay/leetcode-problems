# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:
        if root != None:
            depth = self.getchilddepth(root)
            if depth >= 10000:
                return False
        return True

    def getchilddepth(self, child) -> int:
        if child != None:
            ldepth = 0
            rdepth = 0
            if child.left != None:
                ldepth = self.getchilddepth(child.left)
            if child.right != None:
                rdepth = self.getchilddepth(child.right)
            if ldepth >= 10000 or rdepth >= 10000 or abs(ldepth - rdepth) > 1: # neither left child or right child is balanced
                return 10000
            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1
        return 0
