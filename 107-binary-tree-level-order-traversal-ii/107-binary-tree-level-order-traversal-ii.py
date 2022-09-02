# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        que = deque()
        que.append(root)
        ans = []
        while que:
            size = len(que)
            temp = []
            for _ in range(size):
                cur = que.popleft()
                temp.append(cur.val)
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
            ans.append(temp)
            
        return ans[::-1]