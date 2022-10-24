class Solution:
    def inBound(self, row, col, grid):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
    def backTracking(self, row, col, grid, directions, visited):

        if not self.inBound(row, col, grid) or grid[row][col] == 0 or (row, col) in visited:
            return 0
        visited.add((row, col))
        total = 0
        for dx, dy in directions:
            nextRow, nextCol = row + dx, col + dy
            current =  self.backTracking(nextRow, nextCol, grid, directions, visited)
            total = max(total, current)
        visited.remove((row, col))

        return total + grid[row][col]
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        
        result = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result =  max(result, self.backTracking(i, j, grid, directions, set()))
        return result
                    
        
                            
        