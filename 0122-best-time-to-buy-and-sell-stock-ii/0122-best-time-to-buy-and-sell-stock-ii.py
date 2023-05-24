class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(ind, buyed):
            if ind >= len(prices):
                return 0
            res = dfs(ind + 1, buyed)
            
            # if buyed
            if buyed:
                return max(dfs(ind + 1, not buyed) + prices[ind], res )
        
            else:
                return max(dfs(ind + 1, True) - prices[ind], res)
        
        return dfs(0,False)
    