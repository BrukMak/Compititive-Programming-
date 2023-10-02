class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n = len(dungeon)
        m = len(dungeon[0])
#         @cache
#         def dp(i, j, runningSum, pathMin):
#             if i == n-1 and j == m-1:
#                 runningSum += dungeon[i][j]
#                 pathMin = min(pathMin, runningSum)
#                 return abs(pathMin) + 1
#             if i >= n or j >= m:
#                 return float('inf')
            
#             right = dp(i, j+1, runningSum + dungeon[i][j], min(pathMin, runningSum + dungeon[i][j]))
#             down = dp(i + 1, j, runningSum + dungeon[i][j], min(pathMin, runningSum + dungeon[i][j]))
#             return min(right, down)

#         return dp(0, 0, 0, 0)

        dp = [[float('-inf')] * (m+1) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1:
                    dp[i][j] = min(0, dungeon[i][j])
                else:
                    dp[i][j] = min(0, max(dp[i+1][j], dp[i][j+1]) + dungeon[i][j])
                    
        return abs(dp[0][0]) + 1
                
        