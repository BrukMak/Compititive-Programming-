class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        n = len(matrix)
        val = 1
        for i in range(ceil(n / 2)):
            val = self.rotator([i,i], val, matrix)
        
        return matrix
        
    def rotator(self, start, val, matrix):
        n = len(matrix)
        row, col = start
        # right
        for i in range(col, n):
            if matrix[row][i] != 0:
                break
            matrix[row][i] = val
            val += 1
            col = i
        
        # down 
        for i in range(row+1, n):
            if matrix[i][col] != 0:
                break
            matrix[i][col] = val
            val += 1
            row = i
            
        # left 
        for i in range(col-1, -1, -1):
            if matrix[row][i] != 0:
                break
            matrix[row][i] = val
            val += 1
            col = i
            
        # up 
        for i in range(row-1, -1, -1):
            if matrix[i][col] != 0:
                break
            matrix[i][col] = val
            val += 1
            row = i
        return val
        
        
        