# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if not node:
                return []
            stack = []
            answer = []
            while True:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    if not stack: break
                    node = stack.pop()
                    answer.append(node.val)
                    node = node.right
            return answer
        return inorder(root)
            