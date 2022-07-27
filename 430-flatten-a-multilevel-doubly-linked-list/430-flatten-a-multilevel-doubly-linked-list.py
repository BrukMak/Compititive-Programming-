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
                return node
            
            
            ch = dfs(node.child)
            nxt = dfs(node.next)
            node.child = None
            if ch:
                node.next = ch
                ch.prev = node
            if ch and nxt:
                cur = ch
                while cur.next:
                    cur = cur.next
                cur.next = nxt
                nxt.prev = cur
                
            return node 
            
            
        dfs(head)
        return head
