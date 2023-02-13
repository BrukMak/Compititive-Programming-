class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        N = len(grid)            
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        q = deque()
        q.append((0,0)) 
        visited = {(0, 0)}
        
        
        # finds unvisited clear cells using 8 directions
        def get_neighbours(row,col):
            for x, y in directions:
                new_row = row + x
                new_col = col + y
                
                if 0 <= new_row < N and 0 <= new_col < N and not grid[new_row][new_col] and (new_row, new_col) not in visited:
                    yield (new_row, new_col)                                                
            
        
        curr_distance = 1 
        
        while q:
            length = len(q)
            
            
            for _ in range(length):
                cur = q.popleft()
                print(cur)
                row, col = cur[0], cur[1]
                if row == N-1 and col==N-1: 
                    return curr_distance
                
                for p in get_neighbours(row, col):
                    visited.add(p)
                    q.append(p)
                                    
            curr_distance += 1 
        
        return -1