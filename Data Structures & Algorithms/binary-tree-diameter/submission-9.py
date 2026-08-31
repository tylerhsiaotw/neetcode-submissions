# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def check(node):
            if not node:
                return 0

            right_d = check(node.right)
            left_d = check(node.left)

            self.max_diameter = max(self.max_diameter, right_d + left_d)

            return max(right_d, left_d) + 1
        check(root)
        return self.max_diameter

