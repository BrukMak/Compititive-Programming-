# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSymmetric(node1, node2):
            if not node1:
                return node1 == node2
            if not node2:
                return node2 == node1
            if node1.val != node2.val:
                return False
            return checkSymmetric(node1.left, node2.right) and checkSymmetric(node1.right, node2.left)
        return checkSymmetric(root.left, root.right)
        