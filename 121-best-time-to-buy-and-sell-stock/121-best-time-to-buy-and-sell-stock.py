class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        prev_min = float("inf")
        for i in prices:
            ans = max(ans, i - prev_min )
            if i < prev_min:
                prev_min = i
            
        return ans
    
            