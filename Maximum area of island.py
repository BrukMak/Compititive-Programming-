class Solution:
    def dfs(self, row, col, grid):
        
        if grid[row][col] == 1:
            self.area += 1
            grid[row][col] = 0
            
            if row + 1 < len(grid) and grid[row + 1][col] : self.dfs(row + 1, col, grid)
            if row - 1 >= 0 and grid[row - 1][col]: self.dfs(row - 1, col, grid)
            if col + 1 < len(grid[0]) and grid[row][col + 1]: self.dfs(row, col + 1, grid)
            if col - 1 >= 0 and grid[row][col - 1]: self.dfs(row, col - 1, grid)  
            
        return 
                
            
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.area = 0
                    self.dfs(row,col,grid)
                    ans = max(ans, self.area)
                                        
        return ans
                    
