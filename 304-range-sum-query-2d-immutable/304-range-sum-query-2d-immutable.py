class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        rows, cols = len(matrix)+1, len(matrix[0])+1

        self.prefixSum = [[0] * (cols) for _ in range(rows)]
        
        for i in range(1, rows):
            for j in range(1, cols):
                prevRowPrefix = self.prefixSum[i-1][j]
                prevColPrefix =  self.prefixSum[i][j-1]
                cornerElement = self.prefixSum[i-1][j-1]
                mySelf = matrix[i-1][j-1]
                self.prefixSum[i][j] = prevRowPrefix + prevColPrefix - cornerElement + mySelf
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return self.prefixSum[row2+1][col2+1] - self.prefixSum[row2+1][col1] - self.prefixSum[row1][col2+1] + self.prefixSum[row1][col1]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)