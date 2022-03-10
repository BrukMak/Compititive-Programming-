class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0
        def dfs(ind):
            nonlocal result
            if ind == len(prices)-1:
                return prices[ind]
            max_after = dfs(ind+1)
            result = max(result , max_after - prices[ind])
            return max(max_after, prices[ind])
        dfs(0)
        return result