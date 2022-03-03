class Solution:
    def dfs(self, row, col, grid):
        if grid[row][col] == 0:
            grid[row][col] = 1
            
            if row - 1 >= 0:self.dfs(row - 1, col, grid)
            if row + 1 < len(grid): self.dfs(row + 1, col,grid)
            if col - 1 >= 0: self.dfs(row, col - 1, grid)
            if col + 1 < len(grid[0]):self.dfs(row, col + 1, grid)
            
                
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 0 and (col == 0 or col == len(grid[0]) - 1) or (row == 0 or row == len(grid) - 1):
                    self.dfs(row, col, grid)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 0:
                    self.dfs(row, col, grid)
                    count += 1
        return count
