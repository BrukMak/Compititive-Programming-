class Solution:
    def dfs(self, row, col, grid):
        
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return
        
        self.area += 1
        grid[row][col] = 0

        self.dfs(row + 1, col, grid)
        self.dfs(row - 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row, col - 1, grid)  
             
                
            
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.area = 0
                    self.dfs(row,col,grid)
                    print(self.area)
                    ans = max(ans, self.area)
                                        
        return ans
                    