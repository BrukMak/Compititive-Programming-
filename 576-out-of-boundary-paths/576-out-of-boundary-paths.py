class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int: 
        
        memo = {}
        def dfs(row, col, maxMove):
            if row < 0 or col < 0 or row == m or col == n:
                return 1
            if maxMove <= 0:
                return 0
            if ((row,col),maxMove) in memo:
                return memo[((row, col),maxMove)]
            res = 0
            
            l = dfs(row,col-1, maxMove-1)
            r = dfs(row,col+1, maxMove-1)
            u = dfs(row-1,col, maxMove-1)
            d = dfs(row+1,col, maxMove-1)
            
            res = (l + r + u + d) % (10**9 + 7)
            memo[((row, col),maxMove)] = res
            return memo[((row, col),maxMove)]
                    
        return dfs(startRow, startColumn,maxMove)   
                