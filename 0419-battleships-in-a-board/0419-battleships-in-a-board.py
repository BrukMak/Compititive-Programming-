class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        battleship_count = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    self.dfs(r, c, board, directions)
                    battleship_count += 1
        return battleship_count
    def inBound(self, row, col, board):
        return 0 <= row < len(board) and 0 <= col < len(board[0])
    
    def dfs(self,row, col, board, directions):
        if not self.inBound(row, col, board) or board[row][col] == '.':
            return 
        board[row][col] = '.'
        for r, c in directions:
            new_row = row + r
            new_col = col + c
            self.dfs(new_row, new_col, board, directions)
        
        