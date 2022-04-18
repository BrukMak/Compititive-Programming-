class Solution:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        parent = {}
        size = {}
        self.max_ = 0
        def make_set(t):
            parent[t] = t
            size[t] = 1
        def find(t):
             
            if parent[t] == t:
                return t
            parent[t] = find(parent[t])
            return parent[t]
        def union(t1, t2):
            a = find(t1)
            b = find(t2)
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
                self.max_ = max(self.max_, size[a])
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    tup = (row, col)
                    make_set(tup)
                    self.max_ = max(size[tup], 1)
        
        Dir = [(0, 1),(1, 0), (0, -1), (-1, 0)]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    tup = (row, col)
                    
                    for d in Dir:
                        if 0 <=row + d[0] < rows and 0 <= col + d[1] < cols and grid[row + d[0]][col + d[1]] == 1:
                              union(tup, (row + d[0], col + d[1]))
        
        return self.max_
                    
        
        
        
    