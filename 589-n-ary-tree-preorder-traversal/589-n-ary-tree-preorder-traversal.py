"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        ans = []
        if root: ans.append(root.val)
        def dfs(node):
            if not node: return
            
            temp = node.children
            for i in range(len(temp)):
                
                ans.append(temp[i].val)
                dfs(temp[i])
        dfs(root)
        
        
        
        return ans