class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        @cache
        def dp(i, amount):
            if amount == 0:
                return 0
            if i >= n or amount < 0:
                return inf
            
            take = 1 + dp(i , amount - coins[i])
            skip = dp(i+1, amount)
            
            return min(take, skip)
        
        ans = dp(0, amount)
        return  ans if ans != inf else -1