class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
#         @cache
#         def dfs(idx):
#             if idx == len(arr): return 0
            
#             res = 0
#             val = 0
#             for i in range(idx, min(k+idx,len(arr))):
#                 val = max(val, arr[i])
#                 cur  = dfs(i+1) + val*(i+1- idx)
#                 if cur > res:
#                     res = cur
#             return res
#         return dfs(0)
        dp = [0] * (len(arr) + 1)
        
        for idx in range(len(arr)-1, -1, -1):
            val = 0
            res = 0
            for i in range(idx, min(k+idx,len(arr))):
                val = max(val, arr[i])
                cur = val * (i + 1 - idx) + dp[i+1]
                res = max(res, cur)
            dp[idx] = res
            
        return dp[0]
                
                
                
    