class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        res = float('inf')
        
        # first row right to left prefix sum
        for i in range(n-1, -1, -1):
            if i < n-1:
                grid[0][i] += grid[0][i+1]
                
        # second row left to right prefix sum
        for i in range(n):
            if i > 0:
                grid[1][i] += grid[1][i-1]
        
        # finding the minimum the first player can give
        for i in range(n):
            if i > 0 and i < n-1:
                res = min(res, max(grid[1][i-1], grid[0][i+1]))
            elif i == 0 and i < n-1:
                res = min(res, grid[0][i+1])
            elif i == n - 1 and i > 0:
                res = min(res, grid[1][i-1])
        return res if res != float('inf') else 0
                
       