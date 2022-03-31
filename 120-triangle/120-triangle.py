class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
#         memo = {}
#         def dfs(level, idx):
#             # nonlocal min_path
#             if level == len(triangle) - 1:
#                 return triangle[level][idx]
            
#             if (level,idx) in memo: return memo[(level,idx)]
            
#             path1 = dfs(level + 1, idx)
#             path2 = dfs(level + 1, idx + 1)
            
#             memo[(level,idx)] = min(path1, path2) + triangle[level][idx]
            
#             return memo[(level,idx)]
        
        
#         return dfs(0,0)    
        N = len(triangle)
        
        dp = triangle[-1].copy()
        for level in range(N - 2, -1, -1):
            for idx in range(level+1):
                path1 = dp[idx]
                path2 = dp[idx+1]
                dp[idx] = min(path1, path2) + triangle[level][idx]
            
        return dp[0]
                
                
