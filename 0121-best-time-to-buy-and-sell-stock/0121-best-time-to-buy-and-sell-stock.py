class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        curr_min = prices[0]
        for price in prices:
            ans = max(ans, price - curr_min)
            curr_min = min(price, curr_min)
        return ans
            