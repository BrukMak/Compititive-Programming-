class Solution:
    def inbound(self, r ,c):
        return 0 <= r < self.m and 0 <= c < self.n
    def dfs(self, row, col, grid):
        
        if grid[row][col] == "1":
            grid[row][col] = "v"
            
            if self.inbound(row - 1, col) and grid[row - 1][col]:self.dfs(row - 1, col, grid)
            if self.inbound(row + 1, col) and grid[row + 1][col]:self.dfs(row + 1, col, grid)
            if self.inbound(row, col - 1) and grid[row][col - 1]:self.dfs(row, col - 1, grid)
            if self.inbound(row, col + 1) and grid[row][col + 1]:self.dfs(row, col + 1, grid)
            
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        
        count = 0
        for row in range(self.m):
            for col in range(self.n):
                if grid[row][col] == "1":
                    self.dfs(row, col , grid)
                    count += 1
                    
        return count