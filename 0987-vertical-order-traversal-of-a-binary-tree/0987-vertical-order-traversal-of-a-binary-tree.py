# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.bfs(root)
        
    def bfs(self, root):
        result = defaultdict(list)
        row, col = 0, 0
        q = deque()
        q.append((root, row, col))
        while q:
            size = len(q)
            
            for _ in range(size):
                node, row, col = q.pop()
                result[col].append((row, node.val))
                if node.left:
                    q.append((node.left, row + 1, col - 1))
                if node.right:
                    q.append((node.right, row + 1, col + 1))
        ans = []
        result = dict(sorted(result.items(), key = lambda item:item[0]))
        for val in result.values():
            current = [val for row, val in sorted(val)]
            ans.append(current)
        return ans