class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        memo = {}
        def min_sum_path(row, col):
            
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]
                
            if (row, col) in memo:
                return memo[(row,col)]
            
            if col == len(grid[0]) - 1 and row + 1 < len(grid):
                return grid[row][col] + min_sum_path(row +1, col)
            if row == len(grid) - 1  and col + 1 < len(grid[0]):
                return grid[row][col] + min_sum_path(row, col + 1)

            if row + 1 < len(grid) and col + 1 < len(grid[0]):
                
                memo[(row,col)] = min(min_sum_path(row+1,col), min_sum_path(row, col+1)) + grid[row][col]

            return memo[(row,col)]
        
        return min_sum_path(0,0)