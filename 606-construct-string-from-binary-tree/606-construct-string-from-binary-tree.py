# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def pre(node):
            if not node:
                return ""
            if node.right == node.left:
                return str(node.val)
            if not node.right:
                
                return str(node.val) + '(' + pre(node.left) + ')'
            return str(node.val) + '(' + pre(node.left) + ')(' + pre(node.right) + ')'
        return pre(root)