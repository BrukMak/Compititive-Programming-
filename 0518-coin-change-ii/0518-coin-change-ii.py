class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(i, amount):
            if amount == 0:
                return 1
            if amount < 0 or i >= len(coins):
                return 0
            take = dp(i, amount - coins[i])
            skip = dp(i +1, amount)
            
            return take + skip
    
        return dp(0, amount)