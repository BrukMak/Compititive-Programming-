# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def sum_finder(node):
            if not node:
                return 0
            
            left = 0
            if node.left and not node.left.left and not node.left.right:
                left = node.left.val 
            return sum_finder(node.left) + sum_finder(node.right) + left
            
        return sum_finder(root)
        
            