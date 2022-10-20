# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxMoney(self, node, flag, memo = {}):
        if (node, flag) in memo:
            return memo[(node, flag)]
        if not node:
            return 0
        pick = 0
        skip = 0
        if flag:
            pick = node.val + self.maxMoney(node.left, not flag, memo) + \
            self.maxMoney(node.right, not flag, memo)
            skip = self.maxMoney(node.left, flag) + self.maxMoney(node.right, flag)
        else:
            skip = self.maxMoney(node.left, not flag, memo) + self.maxMoney(node.right, not flag, memo)
        memo[(node, flag)] = max(pick, skip)
        return max(pick, skip)
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.maxMoney(root, True)
        