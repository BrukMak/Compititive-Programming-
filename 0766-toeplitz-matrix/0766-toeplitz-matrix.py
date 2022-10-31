class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row_size = len(matrix)
        col_size = len(matrix[0])
        for row in range(row_size):
            for col in range(col_size):
                check_row = row - 1
                check_col = col - 1
                if self.inBound(check_row, check_col, matrix) and \
                matrix[row][col] != matrix[check_row][check_col]:
                    return False
        return True
        
    def inBound(self, row, col, matrix):
        row_size = len(matrix)
        col_size = len(matrix[0])
        return 0 <= row < row_size and 0 <= col < col_size

    