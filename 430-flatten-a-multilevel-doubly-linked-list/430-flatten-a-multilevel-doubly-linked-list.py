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
            if node.child == node.next:
                return (node, node)
            
            
            ch = dfs(node.child)
            nxt = dfs(node.next)
            node.child = None
            if ch:
                node.next = ch[0]
                ch[0].prev = node
                
            if ch and nxt:
                ch[1].next = nxt[0]
                nxt[0].prev = ch[1]
            return (node, nxt[1]) if nxt else (node, ch[1])
            
            
        dfs(head)
        return head
