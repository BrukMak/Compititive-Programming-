# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        
        def traveller(node, row, col):
            if not node: return
            heappush(res[col], (row, node.val))
            traveller(node.left,row+1, col-1)
            traveller(node.right,row+1, col+1)
        traveller(root, 0, 0)
        res = sorted(res.items())
        ans = []
        for i in res:
            temp = []
            while i[1]:
                temp.append(heappop(i[1])[1])
            ans.append(temp)
        return ans