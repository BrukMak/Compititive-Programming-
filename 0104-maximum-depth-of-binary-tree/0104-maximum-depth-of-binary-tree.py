# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.bfs(root)
    def bfs(self, node):
        if not node:
            return 0
        q = deque()
        answer = 0
        q.append(node)
        while q:
            size = len(q)
            answer += 1
            for _ in range(size):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return answer