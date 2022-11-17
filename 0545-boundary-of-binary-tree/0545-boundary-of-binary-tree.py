# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left:
            left = [root.val]
        else:
            left = self.leftBound(root, [])
        leaf = self.leafNodes(root, [])
        right = self.rightBound(root.right, [])
        # print(self.leftBound(root, []), self.leafNodes(root, []), self.rightBound(root.right, []))
        return left + leaf + right[::-1]
    def leftBound(self, node, boundary):
        if not node: 
            return [] 
        # if not node.left:
        #     return [node.val]
        if node.right == node.left:
            return []
        boundary.append(node.val)
        if node.left:
            l = self.leftBound(node.left, boundary)
        else:
            r = self.leftBound(node.right, boundary)
        return boundary
    def leafNodes(self, node, boundary):
        if not node:
            return []
        if node.left == node.right:
            boundary.append(node.val)
            return []
        self.leafNodes(node.left, boundary)
        self.leafNodes(node.right, boundary)
        return boundary
    def rightBound(self, node, boundary):
        if not node: return []
        if node.left == node.right:
            return []
        boundary.append(node.val)
        r = self.rightBound(node.right, boundary)
        if not node.right:
            l = self.rightBound(node.left, boundary)
        return boundary
    