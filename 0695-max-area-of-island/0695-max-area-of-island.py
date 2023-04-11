class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    result = max(result, self.dfs(r, c, 0, directions, grid))
                    
        return result
    
    def inbound(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])
    def dfs(self,row, col, val, directions, grid):
        if not self.inbound(row, col, grid) or grid[row][col] == 0:
            return val
        grid[row][col] = 0 

        for r, c in directions:
            val = self.dfs(row + r, col + c, val, directions, grid)
        return val + 1