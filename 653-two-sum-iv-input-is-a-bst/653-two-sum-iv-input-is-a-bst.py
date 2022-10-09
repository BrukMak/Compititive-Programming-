# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inO = []
        def inorder(node):
            if not node: return
            
            inorder(node.left)
            inO.append((node, node.val))
            inorder(node.right)
        inorder(root)
        def find(node, cur, cN):
            if not node: return False
            l, r = False, False
            if node.val == cur and cN != node: return True
            elif node.val < cur: 
                l = find(node.right, cur, cN)
            else: 
                r = find(node.left, cur, cN)
            return l or r
        # print(inO)
        for i in inO:
            if find(root, k - i[1], i[0]): return True
        
        return False
            
        
            