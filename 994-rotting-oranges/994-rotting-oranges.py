from collections import deque
class Solution:
    def inbound(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.rows = len(grid)
        self.cols = len(grid[0])
        count = 0
        queue = deque()
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                
                for d in Dir:
                    if self.inbound(r + d[0], c + d[1]) and grid[r + d[0]][c + d[1]] == 1:
                        grid[r + d[0]][c + d[1]] = 2
                        queue.append((r+d[0], c + d[1]))
            count += 1
            
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    return -1
        if count:
            return count - 1
        return 0
                    
            
            