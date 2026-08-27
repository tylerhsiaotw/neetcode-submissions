# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        right_res = self.invertTree(root.right)
        left_res = self.invertTree(root.left)

        root.right = left_res
        root.left = right_res

        return root
        