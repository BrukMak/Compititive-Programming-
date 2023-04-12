class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        return max(self.dfs(grid, i, j, visited, 0) for i in range(len(grid)) for j in range(len(grid[0])))

    def dfs(self, grid, i, j, visited, path_len):
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        if (i, j) in visited or not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1):
            return path_len
        visited.add((i, j))
        
        for dx, dy in dirs:
            nx, ny = i + dx, j + dy
            path_len = self.dfs(grid, nx, ny, visited, path_len)
    
        return path_len + 1