# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[1]
        
    def helper(self, node):
        if not node:
            return (0, True)
        left, right = 0, 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        if abs(left[0] - right[0]) > 1:
            return (0, False)
        
        return (max(left[0], right[0]) + 1, left[1] and right[1])
                        