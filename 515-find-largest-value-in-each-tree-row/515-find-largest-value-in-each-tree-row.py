# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        queue = deque()
        queue.append(root)
        ans = []
        
        
        while queue:
            temp = float(-inf)
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                temp = max(temp, cur.val)
            ans.append(temp)
        
        return ans
        
                