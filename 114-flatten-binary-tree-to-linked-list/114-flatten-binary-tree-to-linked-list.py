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
                return node
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            curL = l
            while curL and curL.right:
                curL = curL.right
                
            if l:
                curL.right = r
                node.right = l
            node.left = None
            
            return node
            
        dfs(root)
        
        