# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        temproot = root
        if temproot != None:
            root = self.swichtree(temproot)
        return root

    def swichtree(self,root):
        cur_root = None
        if root != None:
            cur_root = root
            if root.left != None:
                print(root.left.val)
                cur_root.left = self.swichtree(root.left)
            if root.right != None:
                print(root.right.val)
                cur_root.right = self.swichtree(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
        return cur_root
