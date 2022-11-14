class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        answer = []
        self.backTrack(0, board, answer, n)
        return answer
        
    def backTrack(self, col, board, answer, n):
        if col == n:
            current = []
            for r in board:
                current.append("".join(r))
            answer.append(current)
            return
        for row in range(n):
            if self.checkQueen(row, col, board, n):
                board[row][col] = 'Q'
                self.backTrack(col + 1, board, answer, n)
                board[row][col] = '.'
    def checkQueen(self, row, col, board, n):
        for i in range(n):
            if board[row][i] == 'Q' or board[i][col] == 'Q':
                return False
        left_top_row, left_top_col = row - min(row, col), col - min(row, col)
        while left_top_row < n and left_top_col < n:
            if board[left_top_row][left_top_col] == 'Q':
                return False
            left_top_row += 1
            left_top_col += 1
        # right_top_row, right_top_col = row - (n - 1 - col), col + (n - 1 - col) PROBLEMATIC
        change = min(row, n - 1 - col)
        right_top_row, right_top_col = row - change, col + change
        while right_top_row < n and right_top_col >= 0:
            if board[right_top_row][right_top_col] == 'Q':
                return False
            right_top_row += 1
            right_top_col -= 1
        return True
    