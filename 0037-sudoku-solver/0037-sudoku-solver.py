class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ans = []
        group = []
        for i in range(3):
            group.append([i for i in range(i * 3, ((i + 1) * 3))])
            
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    end_row = r
                    end_col = c
        
        self.backTrack(0, 0 , board, group, end_row, end_col)
        
    def isValid(self, row, col, candidate, board, group):
        for i in range(9):
            if board[i][col] == str(candidate) or board[row][i] == str(candidate):
                return False
        
        for row_arr in group:
            if row in row_arr:
                for col_arr in group:
                    if col in col_arr:
                        for r in row_arr:
                            for c in col_arr:
                                if board[r][c] == str(candidate):
                                    return False
        return True
    
    
    def  backTrack(self,row, col, board, group, end_row, end_col):
        if row == end_row and col == end_col:
            return True
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for candidate in range(1, 10):
                        if self.isValid(r, c, candidate, board, group):
                            board[r][c] = str(candidate)
                            if self.backTrack(r, c, board, group, end_row, end_col):
                                return True
                            else:
                                board[r][c] = "."
                    return False
                            
                    