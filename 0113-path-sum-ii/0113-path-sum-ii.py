# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def dfs(node, cur, sum_):
            if not node:
                return
            
            if not node.left and not node.right:
                sum_ += node.val
                cur.append(node.val)
                if sum_ == targetSum:
                    ans.append(cur.copy())
                sum_ -= node.val
                cur.pop()
                return
            cur.append(node.val)
            sum_ += node.val
            dfs(node.left, cur, sum_)
            dfs(node.right, cur, sum_)
            cur.pop()
            sum_ -= node.val
            return ans
        dfs(root, [], 0)
        return ans