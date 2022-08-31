class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        incomming = [0] *(rows*cols)
        graph = defaultdict(list)
        dxn = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(rows):
            for c in range(cols):
                
                for dr, dc in dxn:
                    nr, nc = r+dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[r][c] < matrix[nr][nc]:
                        
                        graph[r*cols + c].append(nr*cols + nc)
                        incomming[nr*cols + nc] += 1
        que = deque()
        for i, v in enumerate(incomming):
            if v == 0: que.append(i)
        res = 0
        while que:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                for node in graph[cur]:
                    incomming[node] -= 1
                    if incomming[node] == 0:
                        que.append(node)

            res += 1
        return res
                
                
                