# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        value1 = p.val
        value2 = q.val
        if value2 < value1:
            value1, value2 = value2, value1  # value1 < value2
        res = self.compare_val_and_go_on(root, value1, value2)
        return res

    def compare_val_and_go_on(self, root: TreeNode, value1: int, value2: int) -> 'TreeNode':
        rootval = root.val
        if value1 <= rootval <= value2:
            return root
        elif value1 < rootval and value2 < rootval:
            return self.compare_val_and_go_on(root.left, value1, value2)
        if value1 > rootval and value2 > rootval:
            return self.compare_val_and_go_on(root.right, value1, value2)
