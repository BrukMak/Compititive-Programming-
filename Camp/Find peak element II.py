from heapq import heappush,heappop
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        for row in range(len(mat)):
            maxheap = []
            for col in range(len(mat[row])):
                heappush(maxheap, (-mat[row][col] ,(row , col)))
            
            (val , (r,c)) = heappop(maxheap)
            if r < len(mat)-1 and -val > mat[r+1][c]:
                return [r,c]
            elif r < len(mat)-1 and -val < mat[r+1][c]:
                continue
            else:
                return [r, c]

            
                    
