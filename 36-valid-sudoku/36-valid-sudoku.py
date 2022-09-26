class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            cntR = defaultdict(int)
            cntC = defaultdict(int)
            for j in range(9):
                if board[i][j] != "." and board[i][j] not in cntR:
                    cntR[board[i][j]] += 1
                elif board[i][j] in cntR:
                    return False
                
                if board[j][i] != "." and board[j][i] not in cntC:
                    cntC[board[j][i]] += 1
                elif board[j][i] in cntC:
                    return False
                
        for i in range(3):
            for j in range(3):
                cnt = defaultdict(int)
                for row in range(i*3, (i*3 + 3)):
                    for col in range(j*3, (j*3 + 3)):
                        if  board[row][col] in cnt:
                            return False
                        if board[row][col] != ".": cnt[board[row][col]] += 1
        return True
