# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        change = False
        
        while queue:
            
            size = len(queue)
            newlist = []
            for i in range(size):
                
                cur = queue.popleft()
                newlist.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if change:
                newlist = newlist[::-1]
            ans.append(newlist)
            change = not change
        return ans