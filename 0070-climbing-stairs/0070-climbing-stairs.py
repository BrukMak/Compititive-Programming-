class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dp(i):
            if i == n:
                return 1
            if i > n:
                return 0
            one = dp(i+1)
            two = dp(i+2)
            
            return one + two
        return dp(0)
            