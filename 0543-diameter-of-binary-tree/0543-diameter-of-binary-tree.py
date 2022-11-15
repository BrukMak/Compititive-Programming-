# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]
        self.helper(root, max_diameter)
        return max_diameter[0]
    def helper(self, node, max_diameter):
        if not node:
            return 0
        left = self.helper(node.left, max_diameter)
        right = self.helper(node.right, max_diameter)
        max_diameter[0] = max(max_diameter[0], left + right)
        return max(left, right) + 1