class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices += [-inf]
        ans = 0
        l = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                ans += prices[i-1]-prices[l]
                l = i
            
        
        return ans
    