# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def check(node):
            if not node:
                return 0
            left_d = check(node.left)
            right_d = check(node.right)

            if right_d == -1 or left_d == -1:
                return -1

            if abs(left_d - right_d) > 1:
                return -1
            else:
                return max(left_d, right_d) + 1
        return check(root) != -1
        