class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        def dfs(row, col):
            nonlocal perimeter
            
            Dir = [[0,1], [0, -1], [1, 0], [-1, 0]]
            
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                perimeter += 1
            
            elif grid[row][col] == 1:
                grid[row][col] = 2
                for d in Dir:
                    
                    dfs(row + d[0], col + d[1])
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    
        return perimeter
            