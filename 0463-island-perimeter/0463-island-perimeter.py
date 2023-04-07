class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # def islandPerimeter(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        # self.up, self.down, self.right, self.left = 0, 0, 0, 0
        visit = set()

        def dfs(i, j):
            if i >= row or j >= col:
                return 1
            if i < 0 or j < 0:
                return 1
            if grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0
            
            visit.add((i,j))
            up = dfs(i+1, j)
            down = dfs(i-1, j)
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            return up + down + left + right

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return dfs(i, j)