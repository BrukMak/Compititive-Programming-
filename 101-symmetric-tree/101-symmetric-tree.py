# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    def compare(self, level): 
        
        start , end = 0 , len(level)-1
        while start <= end:
            start_node = level[start]
            end_node = level[end]
            if start_node and not end_node or (not start_node and end_node ) : return False     
            if start_node and end_node and  start_node.val != end_node.val: return False 
            start += 1
            end -= 1
        return True
        
            
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque()
        queue.append(root)
        
        while queue: 
            size = len(queue)
            level= []
            for i in range(size):
                level.append(queue.popleft())
            if not self.compare(level): return False
            
            for node in level: 
                if node: 
                    if node.left: 
                        queue.append(node.left)
                    else:
                        queue.append(None)
                    if node.right: 
                        queue.append(node.right)
                    else:
                        queue.append(None)       

        return True    
       
            
            
            