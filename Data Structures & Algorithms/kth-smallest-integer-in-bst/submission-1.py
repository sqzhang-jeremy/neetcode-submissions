# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # find the kth smallest value -> inorder dfs and then pick the kth value
        counter = 0
        answer = None

        def inorder(node):
            nonlocal counter, answer
            if not node or answer is not None:
                return 

            inorder(node.left)

            counter += 1
            if k == counter:
                answer = node.val
                return 

            inorder(node.right)

        inorder(root)

        return answer


        