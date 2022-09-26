class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sub_box = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] in row[r]: return False
                if board[r][c] in col[c]: return False
                if board[r][c] in sub_box[(r // 3, c // 3)]: return False
                
                if board[r][c] != ".":
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    sub_box[(r // 3, c // 3)].add(board[r][c])
                
        return True
