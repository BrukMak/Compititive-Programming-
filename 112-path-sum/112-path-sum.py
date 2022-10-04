# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def pathSum(node, sum_):
            if not node:
                return
            if node.left == node.right:
                return sum_ + node.val == targetSum
            return pathSum(node.left, sum_ + node.val) or pathSum(node.right, sum_ + node.val)
        
        return pathSum(root, 0)
        
            