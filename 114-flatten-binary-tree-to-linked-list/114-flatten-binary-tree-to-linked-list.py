# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(node):
            if not node:
                return
            
            if node.left == node.right:
                return (node, node)
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            node.left = None
            
            if l:
                node.right = l[0]
                
            if r and l:
                l[1].right = r[0]
                
            return (node, r[1])  if r else (node, l[1])
                
            
                
            
        dfs(root)
        
        