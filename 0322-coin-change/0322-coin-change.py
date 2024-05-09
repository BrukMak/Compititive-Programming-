class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
#         @cache
#         def dp(i, amount):
#             if amount == 0:
#                 return 0
#             if i >= n or amount < 0:
#                 return inf
            
#             take = 1 + dp(i , amount - coins[i])
#             skip = dp(i+1, amount)
            
#             return min(take, skip)
        
#         ans = dp(0, amount)
#         return  ans if ans != inf else -1
    
    
    
        dp = [[inf] * (amount+1) for _ in range(n+1)]
        dp[n][0] = 0        
        
        for i in range(n-1, -1, -1):
            for j in range(amount+1):
                take = inf
                if j - coins[i] >= 0:
                    take = 1 + dp[i][j - coins[i]]
                skip = dp[i+1][j]
                
                dp[i][j] = min(take, skip)
                
        ans = dp[0][amount]
        return ans if ans != inf else -1