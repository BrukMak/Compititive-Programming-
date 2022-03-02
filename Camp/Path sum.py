# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, prev_sum):
            if not node:
                return False
            if node.right == node.left:
                return prev_sum + node.val == targetSum
            
            left_result = dfs(node.left, prev_sum + node.val)
            right_result = dfs(node.right, prev_sum + node.val)
            
            return left_result or right_result
        return dfs(root, 0)
