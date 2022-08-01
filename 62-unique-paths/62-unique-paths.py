class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(row, col):
            if row >= m or col >= n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            
            down = dfs(row + 1, col)
            right = dfs(row, col + 1)
            return down + right
        return dfs(0,0)
            