# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        num_nodes_left = self.count_nodes(root.left)
        if k <= num_nodes_left:
            return self.kthSmallest(root.left, k)
        if k == num_nodes_left + 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k - 1 - num_nodes_left)
        # the mutation method didn't work
        # for i in range(k - 1):
        #     self.get_smallest_and_remove(root)
        # self.remove_smallest_k_times(root, k - 1)
        # return self.get_smallest(root)  # this root is the original root

    def count_nodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return self.count_nodes(root.left) + 1 + self.count_nodes(root.right)

    # def remove_smallest_k_times(self, root: TreeNode | None, k: int) -> None:
    #     while k > 0:
    #         if root is None:
    #             return
    #         if root.left is None:  # root is the smallest
    #             root = root.right
    #             return self.remove_smallest_k_times(root, k - 1)
    #         if root.left is not None:
    #             return self.remove_smallest_k_times(root.left, k)
    #
    # def get_smallest(self, root: TreeNode) -> int | None:
    #     if root.left is None:  # root is the smallest
    #         return root.val
    #     else:
    #         return self.get_smallest(root.left)
