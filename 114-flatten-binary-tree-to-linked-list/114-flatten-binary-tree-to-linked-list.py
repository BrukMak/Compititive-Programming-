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
            
                
            if l and r:
                l[1].right = r[0]
                node.right = l[0]
                node.left = None
                return (node, r[1])
            elif l:
                node.right = l[0]
                node.left = None
                return (node, l[1])
            else:
                node.left = None
                return (node, r[1])
            
        dfs(root)
        
        