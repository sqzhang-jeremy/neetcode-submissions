# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # find the kth smallest value -> inorder dfs and then pick the kth value

        order_tree = []

        def inorder(node):

            if not node:
                return 

            inorder(node.left)
            order_tree.append(node.val)
            inorder(node.right)

        inorder(root)

        return order_tree[k - 1]


        