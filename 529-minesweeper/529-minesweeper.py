class Solution:
    def inbound(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols
    def isadj(self, r, c,board):
        self.Dir = [(-1,-1), (-1,0), (-1,1), (0,1), (0,-1), (1,-1), (1,0), (1,1)]
        count = 0
        for d in self.Dir:
            if self.inbound(r + d[0], c + d[1]) and board[r + d[0]][ c + d[1]] == "M":
                count += 1
                
        return count
    def dfs(self, row, col, board):
        if self.inbound(row,col):
            if board[row][col] == "M":
                board[row][col] = "X"
                return
            elif board[row][col] == "E":
                if self.isadj(row,col,board):
                    board[row][col] = str(self.isadj(row, col, board))
                    return
                board[row][col] = "B"
                for d in self.Dir:
                    self.dfs(row + d[0], col + d[1], board)
        return
        
        
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.rows = len(board)
        self.cols = len(board[0])
        col = click.pop()
        row = click.pop()
        
        self.dfs(row, col, board)
        
        return board