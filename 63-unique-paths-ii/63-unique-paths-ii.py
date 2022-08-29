class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        @lru_cache(None)
        def path(row, col):
            if row >= rows or col >= cols or obstacleGrid[row][col] == 1: return 0
            if row == rows-1 and col == cols -1: return 1
            
            return path(row+1, col) + path(row, col + 1)
        
        return path(0, 0)