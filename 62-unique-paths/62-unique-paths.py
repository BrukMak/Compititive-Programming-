class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        # @lru_cache(None)
        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            if row >= m or col >= n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            
            down = dfs(row + 1, col)
            right = dfs(row, col + 1)
            memo[(row,col)] = down + right
            return memo[(row,col)]
        return dfs(0,0)
            