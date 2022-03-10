class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(idx, can_buy):
            
            if idx >= len(prices):
                return 0
            if(idx, can_buy) in memo:
                return memo[(idx, can_buy)]
            else:
                if can_buy:
                    memo[(idx, can_buy)] = max(dp(idx + 1, not can_buy) - prices[idx], dp(idx + 1, can_buy) )
                    return memo[(idx, can_buy)]
                else:
                    memo[(idx, can_buy)] = max(dp(idx + 2, not can_buy) + prices[idx] , dp(idx+1,can_buy))
                    return memo[(idx, can_buy)]
        
        return dp(0, True)