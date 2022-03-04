class Solution:
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0]) 
        
        def isEdge(r, c):
            return (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)
               
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if board[r][c] == "X" or board[r][c] == "$":
                return 
            
            board[r][c] = "$"
            
            dfs(r, c - 1)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r + 1, c)
                
                
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and isEdge(r, c):
                    dfs(r, c)
                    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "$":
                    board[r][c] = "O"
            
              
                    
    