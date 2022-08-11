# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxHeight = 0
        def dfs(node, curHeight):
            nonlocal maxHeight
            if not node:
                return
            if node.left == node.right:
                maxHeight = max(maxHeight, curHeight)
                return 
            curHeight += 1
            dfs(node.left, curHeight)
            dfs(node.right, curHeight)
            
        dfs(root, 1)
        return maxHeight