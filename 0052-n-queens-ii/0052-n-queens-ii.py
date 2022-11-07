class Solution:
    def totalNQueens(self, n: int) -> int:
        answer = [0]
        board = [["."] * n for _ in range(n)]
        self.backTrack(0, answer, board, n)
        return answer[0]
    
    def backTrack(self, row, answer, board, n):
        if row == n:
            answer[0] += 1
            return    
        
        for col in range(n):
            if self.checkQueen(row, col, board, n):
                board[row][col] = "Q"
                self.backTrack(row + 1, answer, board, n)
                board[row][col] = "."
                
                
    def checkQueen(self, row, col, board, n):
        for i in range(n):
            if board[row][i] == "Q" or board[i][col] == "Q":
                return False
        ltr, ltc = row - min(row, col), col - min(row, col)
        while ltr < n and ltc < n:
            if board[ltr][ltc] == "Q":
                return False
            ltr += 1
            ltc += 1
            
        rtr, rtc = row - (n - 1 - col), col + (n - 1 - col)
        while rtr < n and rtc >= 0:
            if board[rtr][rtc] == "Q":
                return False
            rtc -= 1
            rtr += 1
        return True
    
            
            