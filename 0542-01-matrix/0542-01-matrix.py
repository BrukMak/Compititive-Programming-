import math
class Solution:
    def inBound(self, r, c, mat):
        return 0 <= r < len(mat) and 0 <= c < len(mat[0])
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[math.inf] * len(mat[0]) for _ in range(len(mat))]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        que = deque()
        
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if not mat[r][c]:
                    que.append((r, c))
                    ans[r][c] = 0 
        
        while que:
            r, c = que.popleft()
            
            for rD, cD in direction:
                newR = rD + r
                newC = cD + c
                if self.inBound(newR, newC, mat) and ans[newR][newC] > ans[r][c] + 1:
                    ans[newR][newC] = ans[r][c] + 1
                    que.append((newR, newC))
        return ans
            

            

        
                    