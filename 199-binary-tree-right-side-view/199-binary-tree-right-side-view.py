# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        level = set()
        def dfs(node, lev):
            if not node:
                return
            if lev not in level:
                level.add(lev)
                ans.append(node.val)
            dfs(node.right, lev + 1)
            dfs(node.left, lev + 1)
        
        dfs(root, 0)
        print(ans)
        
        return ans
                    
            
        