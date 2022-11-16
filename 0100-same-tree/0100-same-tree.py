# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.inorder(p, q)
        
    def inorder(self, node1, node2):
        if not node1 or not node2:
            return node1 == node2
        if node1.val != node2.val:
            return False
        left = self.inorder(node1.left, node2.left)
        right = self.inorder(node1.right, node2.right)
        if not left or not right:
            return False
        return left and right
        