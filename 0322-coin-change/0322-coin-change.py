class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
#         def minCoins(i, amount):
#             if amount == 0:
#                 return 0
#             if amount < 0 or i >= len(coins):
#                 return float('inf')
            
#             take = float('inf')
#             if amount - coins[i] >=0:
#                 take = 1 + minCoins(i, amount - coins[i])
#             skip = minCoins(i+1, amount)
            
#             return min(take, skip)
#         res = minCoins(0, amount)
#         return res if res != float('inf') else -1
    
    
        """
        Top Down:
            Base Case:
                amount = 0: return 0
                amount < 0 or i >= len(coins): return inf
            
            State transition:
                i: 0 => n
                amount: amount => 0
        
        """
        n = len(coins)
        dp = [[float('inf')] *(amount+1) for _ in range(n+1)]
        dp[n][0] = 0
        
        for i in range(n-1, -1, -1):
            for j in range(amount + 1):
                take = float('inf')
                if j - coins[i] >= 0:
                    take = 1 + dp[i][j - coins[i]]
                skip = dp[i+1][j]
                
                dp[i][j] = min(take, skip)
        return dp[0][amount] if dp[0][amount] != float('inf') else -1
        
        
        
        
        
        
        