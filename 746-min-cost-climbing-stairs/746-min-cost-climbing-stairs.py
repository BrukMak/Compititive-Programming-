class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        di ={}
        def out_of_bound(idx):
            return idx >= len(cost)
        
        def dp(idx):
            if out_of_bound(idx):
                return 0
            if idx in di: return di[idx]
            
            by_one = dp(idx + 1)
            by_two = dp(idx + 2)

            di[idx] = min(by_one, by_two) + cost[idx]
            
            return di[idx]
        
        return min(dp(0), dp(1))