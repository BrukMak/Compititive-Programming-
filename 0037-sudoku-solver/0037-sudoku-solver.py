class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ans = []
    
            
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    end_row = r
                    end_col = c
        
        self.backTrack(0, 0 , board, end_row, end_col)
        
    def isValid(self, row, col, candidate, board):
        for i in range(9):
            if board[i][col] == str(candidate) or board[row][i] == str(candidate):
                return False
            if board[3 * (row // 3 ) + (i // 3)][3 * (col // 3) + (i % 3)] == str(candidate):
                return False
        return True
    
    
    def  backTrack(self,row, col, board, end_row, end_col):
        if row == end_row and col == end_col:
            return True
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in range(1, 10):
                        if self.isValid(r, c, num, board):
                            board[r][c] = str(num)
                            if self.backTrack(r, c, board, end_row, end_col):
                                return True
                            else:
                                board[r][c] = "."
                        
                    return False
                            
                    