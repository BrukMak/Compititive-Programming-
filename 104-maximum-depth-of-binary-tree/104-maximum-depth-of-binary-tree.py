# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def max_depth(node, depth):
            nonlocal ans
            if not node:
                return
            if node.right == node.left:
                ans = max(ans, depth+1)
            max_depth(node.left, depth + 1)
            max_depth(node.right, depth + 1)
        max_depth(root, 0)
        return ans