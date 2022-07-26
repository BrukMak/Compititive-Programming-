# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        top = float('inf')
        def dfs (node):
            nonlocal top
            if not node:
                return True
            left = dfs(node.left)
            if top == float('inf') or top < node.val:
                top = node.val
            else:
                return False
            right = dfs(node.right)
            return left and right
        return dfs(root)
        
            
             
            