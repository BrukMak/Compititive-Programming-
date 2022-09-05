"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        ans = [[root.val]]
        queue.append(root)
        
        while queue:
            
            size = len(queue)
            temp = []
            for _ in range(size):
                cur = queue.popleft()
                if cur.children:
                    for child in cur.children:
                        temp.append(child.val)
                        queue.append(child)
            if temp:
                ans.append(temp)
            
        return ans