class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        def inbound(r, c):
            return 0 <= r < len(land) and 0 <= c < len(land[0])
        
        def bfs(r, c):
            directions = [0, 1, 0, -1, 0]
            queue = deque()
            queue.append((r, c))
            land[r][c] = 0
            
            
            while queue:
                cur_row, cur_col = queue.popleft()
                for i in range(len(directions)-1):
                    row_addition = directions[i]
                    col_addition = directions[i+1]
                    new_r = cur_row + row_addition
                    new_c = cur_col + col_addition
                    
                    if inbound(new_r, new_c) and land[new_r][new_c]:
                        queue.append((new_r, new_c))
                        land[new_r][new_c] = 0
                
                if not queue:
                    return [cur_row, cur_col]
                        
        result = []
        
        for start_row in range(len(land)):
            for start_col in range(len(land[0])):
                if land[start_row][start_col]:
                    
                    end_row, end_col = bfs(start_row, start_col)
                    result.append([start_row, start_col, end_row, end_col])
                    
        return result
                        
                    
                    
                
                
            