# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.find(root)
        
        return self.res
        
    def find(self, node):
        if not node:
            return 0

        left = self.find(node.left)
        right = self.find(node.right)
        self.res += abs(left - right)
        return node.val + left + right
        