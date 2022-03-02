from heapq import heapify, heappush, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxheap = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if len(maxheap) < k:
                    heappush(maxheap, -matrix[i][j])
                elif len(maxheap) == k:
                    if matrix[i][j] < -maxheap[0]:
                        heappop(maxheap)
                        heappush(maxheap, -matrix[i][j])
        
            
        return -heappop(maxheap)
