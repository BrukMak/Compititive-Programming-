# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        prefixSum = defaultdict(int)
        prefixSum[0] += 1
        self.validCounter(root, 0, prefixSum, targetSum)
        return self.paths
        
    # Doing subarray sum equal to k while traversing the tree
    def validCounter(self, node, runningSum, prefixSum, targetSum):
        if not node:
            return 0
        
        runningSum += node.val
        checkVal = runningSum - targetSum
        if checkVal in prefixSum:
            self.paths += prefixSum[checkVal]
        prefixSum[runningSum] += 1
        self.validCounter(node.left, runningSum, prefixSum, targetSum)
        self.validCounter(node.right, runningSum, prefixSum, targetSum)
        prefixSum[runningSum] -= 1
        runningSum -= node.val
        