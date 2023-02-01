class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        ans = [[0] * cols for _ in range(rows)]
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                start_i = max(1, i-k)
                start_j = max(1, j-k)
                
                end_i = min(rows, i+k)
                end_j = min(cols, j+k)
                
                ans[i-1][j-1] = prefix[end_i][end_j] - prefix[start_i-1][end_j] - prefix[end_i][start_j-1] + prefix[start_i-1][start_j-1]
                
        return ans