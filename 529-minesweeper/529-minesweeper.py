class Solution:
    def inbound(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols
    def isadj(self, r, c,board):
        count = 0
        if self.inbound(r - 1, c - 1) and board[r - 1][c - 1] == "M":
            count += 1
        if self.inbound(r - 1, c) and board[r - 1][c] == "M":
            count += 1
        if self.inbound(r - 1, c + 1) and board[r - 1][c + 1] == "M":
            count += 1
        if self.inbound(r + 1, c + 1) and board[r + 1][c + 1] == "M":
            count += 1
        if self.inbound(r + 1, c) and board[r + 1][c] == "M":
            count += 1
        if self.inbound(r + 1, c - 1) and board[r + 1][c - 1] == "M":
            count += 1
        if self.inbound(r, c + 1) and board[r ][c + 1] == "M":
            count += 1
        if self.inbound(r, c - 1) and board[r][c - 1] == "M":
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
                self.dfs(row - 1,col, board)# up
                self.dfs(row, col - 1, board)# Left
                self.dfs(row + 1, col, board)# Down
                self.dfs(row, col + 1, board)# Right
                self.dfs(row - 1,col - 1, board)# up left 
                self.dfs(row + 1, col + 1, board)# down right
                self.dfs(row - 1, col + 1, board)# up right
                self.dfs(row + 1, col - 1, board)# down left
        return
        
        
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.rows = len(board)
        self.cols = len(board[0])
        col = click.pop()
        row = click.pop()
        
        self.dfs(row, col, board)
        
        return board