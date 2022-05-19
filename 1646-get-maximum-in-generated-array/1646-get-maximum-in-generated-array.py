class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        memo = {}
        def dp (idx):
            
            if idx == 1 or idx == 0:
                memo[idx] = idx
                return memo[idx]
            if idx not in memo:
                if idx % 2 == 0:
                    memo[idx] = dp(idx//2)
                else:
                    memo[idx] = (dp(idx//2 + 1)+dp(idx//2))
            return memo[idx]
        
        for i in range(n+1):
            dp(i)
        return max(memo.values())