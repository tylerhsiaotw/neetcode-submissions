# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def same(r, sr):
            if not r and not sr:
                return True
            elif not r or not sr:
                return False
            elif r.val != sr.val:
                return False
            return same(r.right, sr.right) and same(sr.left, r.left)

        if same(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)


