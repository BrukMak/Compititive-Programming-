# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return 0
        ans = []
        queue = deque()
        
        queue.append(root)
        
        while queue:
            
            size = len(queue)
            level_sum = 0
            for _ in range(size):
                cur = queue.popleft()
                level_sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                    
                if cur.right:
                    queue.append(cur.right)
            ans.append(level_sum / size)
            
        return ans