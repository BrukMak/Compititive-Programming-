class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        battleship_count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                up = r - 1
                left = c - 1
                if board[r][c] == 'X':
                    if (up >= 0 and board[up][c] == 'X') or (left >= 0 and board[r][left] == 'X'):
                        continue
                    else:
                        battleship_count += 1
                
        return battleship_count
