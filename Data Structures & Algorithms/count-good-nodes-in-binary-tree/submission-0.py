# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            if not node:
                return 0

            good = 1 if node.val >= max_so_far else 0
            
            left = dfs(node.left, max(node.val, max_so_far))
            right = dfs(node.right, max(node.val, max_so_far))

            return left + right + good
        return dfs(root, root.val)