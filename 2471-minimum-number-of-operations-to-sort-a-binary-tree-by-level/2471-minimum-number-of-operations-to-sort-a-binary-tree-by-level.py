# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        return self.bfs(root)
    
    def bfs(self, node):
        visited = set()
        q = deque()
        q.append(node)
        swaps = 0
        while q:
            size = len(q)
            cur_list = []
            for n in q:
                cur_list.append(n.val)
            
            swaps += self.count(cur_list, visited)
            # print(swaps)
            for _ in range(size):
                cur = q.popleft()
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
        return swaps
    
    def count(self, cur_list, visited):
        
        cur_list = [*enumerate(cur_list)]
        cur_list.sort(key = lambda it: it[1])
        count = 0
        for i in range(len(cur_list)):
            if i == cur_list[i][0] or cur_list[i][1] in visited:
                continue
            
            cycle = 0
            j = i
            while cur_list[j][1] not in visited:
                visited.add(cur_list[j][1])
                j = cur_list[j][0]
                cycle += 1
            count += cycle - 1 if cycle else 0
            
        return count
                
                
