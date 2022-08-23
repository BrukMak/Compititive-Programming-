class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        rowMax = []
        colMax = []
        for i in grid:
            rowMax.append(max(i))
        for col in range(n):
            cur = 0
            for row in range(n):
                cur = max(cur, grid[row][col])
            colMax.append(cur)
                
        
        for row in range(n):
            for col in range(n):
                ans += min(rowMax[row], colMax[col]) - grid[row][col]
        return ans