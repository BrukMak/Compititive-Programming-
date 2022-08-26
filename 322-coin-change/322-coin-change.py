class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def uk(idx, amount):
            if idx >= len(coins) and amount == 0 or amount == 0:
                return 0
            if idx >= len(coins) or amount <0:
                return float('inf')
            
            take = 1 + uk(idx, amount- coins[idx])
            dont = uk(idx + 1, amount)
            
            return min(take, dont)
        ans = uk(0, amount)
        return -1 if ans >= float('inf') else ans