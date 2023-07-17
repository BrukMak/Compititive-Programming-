class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
#         def dp(i):
#             if i >= len(cost):
#                 return 0
            
#             p1 = cost[i] + dp(i+1)
#             p2 = cost[i] + dp(i+2)
            
#             return min(p1, p2)
        
#         return min(dp(0), dp(1))
    
        n = len(cost)
        dp = [0 for _ in range(n+2)]
        
        for i in range(n-1, -1, -1):
            p1 = cost[i] + dp[i+1]
            p2 = cost[i] + dp[i+2]
            
            dp[i] = min(p1, p2)
        return min(dp[0], dp[1])
            
            
            
            