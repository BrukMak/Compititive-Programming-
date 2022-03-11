class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # min_path = 0
        memo = {}
        def dfs(level, idx):
            # nonlocal min_path
            if level == len(triangle) - 1:
                return triangle[level][idx]
            
            if (level,idx) in memo: return memo[(level,idx)]
            
            path1 = dfs(level + 1, idx)
            path2 = dfs(level + 1, idx + 1)
            
            memo[(level,idx)] = min(path1, path2) + triangle[level][idx]
            
            return memo[(level,idx)]
        
        
        return dfs(0,0)