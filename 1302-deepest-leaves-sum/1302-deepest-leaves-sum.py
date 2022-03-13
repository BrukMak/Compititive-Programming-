# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        
        queue.append(root)
        
        while queue:
            sum = 0
            for _ in range(len(queue)):
                cur = queue.popleft()
                sum += cur.val
                if cur.left:queue.append(cur.left)
                if cur.right:queue.append(cur.right)
                
        return sum
            
            