# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        values = []
        
        
        def dfs(node):
            # nonlocal to_be_swaped1,to_be_swaped2,pre
             
            if not node:
                return 
            
            dfs(node.left)
            
            nodes.append(node)
            values.append(node.val)
            
            dfs(node.right)
            
        
        dfs(root)
        values.sort()
        for i in range(len(nodes)):
            nodes[i].val = values[i]
            
                
                