# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def gns(node, maxVal=float('-inf')):
            nonlocal count
            if not node: return
            if node.val >= maxVal:
                count += 1
                maxVal = node.val
            gns(node.left, maxVal)
            gns(node.right, maxVal)
        gns(root)
        return count