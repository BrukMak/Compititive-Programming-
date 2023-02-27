class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        matrix = [[0] * n for _ in range(n)]
        
        for query in queries:
            self.mark(query, matrix)
        print(matrix)
        return self.prefixSum(matrix)
        
    def mark(self, query, matrix):
        r1, c1, r2, c2 = query
        n = len(matrix)
        for r in range(r1, r2+1):
            if 0 <= r < n and 0 <= c1 < n:
                matrix[r][c1] += 1
            if 0 <= r < n and 0 <= c2+1 < n:
                matrix[r][c2+1] -= 1
        
    def prefixSum(self, matrix):
        n = len(matrix)
        
        # horizontal prefix sum 
        for r in range(n):
            for c in range(n):
                if c > 0:
                    matrix[r][c] += matrix[r][c-1]
                    
        return matrix
                    