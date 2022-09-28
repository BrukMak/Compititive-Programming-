class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols =len(matrix[0])
        self.pre = [[0] * (self.cols+1) for _ in range(self.rows + 1)]
        # self.pre[1][1] = matrix[0][0]
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                self.pre[i][j] = self.pre[i-1][j] + self.pre[i][j-1] - self.pre[i-1][j-1] + matrix[i-1][j-1]
        print(self.pre)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        ans = self.pre[row2+1][col2+1] - self.pre[row2+1][col1] - self.pre[row1][col2+1] + self.pre[row1][col1]
        
        return ans
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)