# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.bfs(root, False)
        
    def bfs(self, node, flip):
        if not node:
            return []
        ans = []
        q = deque()
        q.append(node)
        while q:
            size = len(q)
            cur_q = list(q)
            if flip:
                temp_ans = []
                for i in range(len(cur_q)-1, -1, -1):
                    temp_ans.append(cur_q[i].val)
                ans.append(temp_ans)
            else:
                temp_ans = []
                for n in cur_q:
                    temp_ans.append(n.val)
                ans.append(temp_ans)
            flip = not flip
            for _ in range(size):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return ans
                    