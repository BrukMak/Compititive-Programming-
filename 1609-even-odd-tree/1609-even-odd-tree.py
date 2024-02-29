# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        
        queue = deque()
        queue.append(root)
        level = 0
        
        while queue:
            n = len(queue)
            
            for i in range(n):
                value = queue.popleft()
                if level % 2 == 0:
                    if value.val % 2 == 0 or (n > i + 1 and value.val >= queue[0].val):
                        return False
                else:
                    if value.val % 2 or (n > i + 1 and value.val <= queue[0].val):
                        return False
                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)
                
            level += 1
                
        return True
                
                
                    
            