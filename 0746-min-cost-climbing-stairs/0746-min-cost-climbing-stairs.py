class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        @cache
        def dp(i):
            if i >= n:
                return 0
            
            one_step = cost[i] + dp(i+1)
            two_step = cost[i] + dp(i+2)
            
            return min(one_step, two_step)
        
        return min(dp(0), dp(1))    
            