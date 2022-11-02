class Solution:
    answer = 0
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        empty_count = 0
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for row in range(rows):
            for col in range(cols):
                if not grid[row][col]:
                    empty_count += 1
                if grid[row][col] == 1:
                    start_row = row
                    start_col = col
        visited = set()
        visited.add((start_row, start_col))
        self.backTrack(start_row, start_col, 0, empty_count, grid, directions, visited)
        return self.answer
    
    def inBound(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])
    
    
    def backTrack(self, row, col, path, empty_count, grid, directions, visited):

        if path - 1 == empty_count and grid[row][col] == 2:
            # print('here')
            self.answer += 1
            return
        # if (row, col) in visited:
        #     return
        
        for x, y in directions:
            new_row, new_col = row + x, col + y
            
            if self.inBound(new_row, new_col, grid) and grid[new_row][new_col] != -1 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                
                self.backTrack(new_row, new_col, path + 1, empty_count, grid, directions, visited)
                # path -= 1
                visited.remove((new_row, new_col))
        