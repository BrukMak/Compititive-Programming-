class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirxn = [0, 1, 0, -1, 0]
        visited = set()
        def inBound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) 
        def bfs(r, c, visited):
            que = deque([(r,c)])
            visited.add((r,c))
            
            while que:
                cur = que.popleft()
                # visited.add(cur)
                for i in range(len(dirxn)-1):
                    nr, nc = cur[0] + dirxn[i], cur[1] + dirxn[i+1]
                    
                    if inBound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == "1":
                        que.append((nr, nc))
                        visited.add((nr, nc))
        
        numOfIslands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c, visited)
                    numOfIslands += 1
        
        return numOfIslands
                
                    
            