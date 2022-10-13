class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])
        r, c = rows - 1, 0
        for _ in range(rows + cols):
            
            if r < 0 or c == cols:
                return False
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                c += 1
            else:
                r -= 1
        