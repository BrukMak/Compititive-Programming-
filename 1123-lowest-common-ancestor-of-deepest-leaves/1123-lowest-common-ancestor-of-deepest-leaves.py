# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return (node, 0)
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        
        if l[1] == r[1]: return (node, l[1] + 1)
        
        elif l[1] > r[1]: return (l[0], l[1] + 1)
        
        return (r[0], r[1] + 1)
        
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self.dfs(root)[0]