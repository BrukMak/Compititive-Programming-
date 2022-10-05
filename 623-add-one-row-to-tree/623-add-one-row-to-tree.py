# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode
        d_count = 1
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if d_count == depth -1:
                    
                    tempL = cur.left
                    tempR = cur.right
                    cur.left = TreeNode(val)
                    cur.left.left = tempL
                    cur.right = TreeNode(val)
                    cur.right.right = tempR
                    
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            if d_count == depth-1:
                return root
            d_count += 1
        
        
        return 
            
            