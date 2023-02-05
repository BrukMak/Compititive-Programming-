# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append(root)
        depth = 0
        if not root:
            return depth
        while q:
            size = len(q)
            depth += 1
            for _ in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                if not cur.left and not cur.right:
                    return depth
                
        