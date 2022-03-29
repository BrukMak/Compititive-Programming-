class Solution:
    def climbStairs(self, n: int) -> int:
        # count = 0
        visited = {}
        def dp(num):
            
            if num == 1 or num == 0: return 1
            if num not in visited:
                visited[num] = dp(num - 1) + dp(num - 2)
            
            return visited[num]
        
        return dp(n)