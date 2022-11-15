# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.max_depth(root)
    def max_depth(self, node):
        if not node:
            return 0
        left = self.max_depth(node.left)
        right = self.max_depth(node.right)
        return max(left, right) + 1