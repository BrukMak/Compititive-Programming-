from collections import deque
class Solution:
    def inbound(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
    def orangesRotting(self, grid: List[List[int]]) -> int:
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
                if self.inbound(r - 1, c) and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    queue.append((r - 1 , c))
                if self.inbound(r + 1, c) and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    queue.append((r + 1 , c))
                if self.inbound(r, c - 1) and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    queue.append((r , c - 1))
                if self.inbound(r, c + 1) and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    queue.append((r , c + 1))
            count += 1
        # print(grid)
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    return -1
        if count:
            return count - 1
        return 0
                    
            
            