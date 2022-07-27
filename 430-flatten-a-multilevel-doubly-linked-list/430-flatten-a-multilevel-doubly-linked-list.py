"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = []
        def dfs(node):
            if not node:
                return 
            res.append(node)
            
            dfs(node.child)
            dfs(node.next)
        
        dfs(head)
        
        if res: 

            for i in range(1, len(res)):
                res[i].prev = res[i-1]
                res[i-1].next = res[i]
                res[i].child = None
                res[i-1].child = None
            return res[0]
        return None
                
            
        