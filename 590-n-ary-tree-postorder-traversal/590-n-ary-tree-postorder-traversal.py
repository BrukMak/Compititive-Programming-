"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return
            temp  = node.children
            for i in range(len(temp)):
                dfs(temp[i])
                ans.append(temp[i].val)
        dfs(root)
        if root: ans.append(root.val)
        return ans
            
                