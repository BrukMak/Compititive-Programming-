# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = [0]
        self.findPaths(root, [], answer)
        return answer[0]
        
        
    def findPaths(self, node, current, answer):
        if node and not node.left and not node.right:
            current.append(str(node.val))
            answer[0] += int("".join(current))
            return
        if not node:
            return
        
        # current.append(str(node.val))
        self.findPaths(node.left, current + [str(node.val)], answer)
        # current.pop()
        self.findPaths(node.right, current + [str(node.val)], answer)
        # current.pop()
