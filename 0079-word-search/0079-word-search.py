class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0]) 
        dxn = [0,1,0,-1,0]
        
        
        def dfs(r, c, cur_word):
            if len(cur_word) == len(word) and "".join(cur_word) == word:
                print(cur_word, word)
                return True
            if (cur_word and cur_word[-1] != word[len(cur_word)-1]) or len(cur_word) >= len(word) or len(seen) == len(board) * len(board[0]):
                return False
            
            for i in range(1, len(dxn)):
                nr = r + dxn[i-1]
                nc = c + dxn[i]
                if inbound(nr, nc) and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    cur_word.append(board[nr][nc])
                    if dfs(nr, nc, cur_word):
                        return True
                    seen.remove((nr, nc))
                    cur_word.pop()
                
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                seen = set()
                seen.add((r, c))
                if dfs(r, c, [board[r][c]]):
                    return True
                seen.remove((r, c))
        return False
            