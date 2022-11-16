# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = [float('-inf')]
        print(self.helper(root, max_path_sum))
        return max_path_sum[0]
        
    def helper(self, node, max_path_sum):
        if not node:
            return 0
        left = self.helper(node.left, max_path_sum)
        right = self.helper(node.right, max_path_sum)
        
        max_path_sum[0] = max(max_path_sum[0], (left + right + node.val))
        ans = max(left, right, 0) + node.val
        return ans if ans > 0 else 0