# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_diameter = 0

        def max_depth(node):
            if not node:
                return 0

            right_d = max_depth(node.right)
            left_d = max_depth(node.left)

            self.max_diameter = max(self.max_diameter, right_d + left_d)

            return max(right_d, left_d) + 1
        max_depth(root)

        return self.max_diameter
        