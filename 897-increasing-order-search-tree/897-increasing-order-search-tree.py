# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        ans = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
                
        dfs(root)
        
        newNode = TreeNode(ans[0])
        ansNode = newNode
        # newNode = newNode.right
        for i in range(1, len(ans)):
            newNode.right = TreeNode(ans[i])
            newNode = newNode.right
        
        
        return ansNode
            