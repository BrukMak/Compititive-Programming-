class Solution:
    def isEdge(self,row, col):
        return (row == 0 or row == self.rows - 1 or col == 0 or col == self.cols - 1)
    def dfs(self, row, col, grid):
        Dir = [(0,-1), (0, 1), (-1,0), (1,0)]
        if (0 <= row < self.rows and 0 <= col < self.cols) and grid[row][col] == 1 :
            grid[row][col] = 2
            for d in Dir:
                self.dfs(row + d[0], col + d[1], grid)
        return
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 1 and self.isEdge(r, c):
                    self.dfs(r,c,grid)
        
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 1:
                    count += 1
        
        return count