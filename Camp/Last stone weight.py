from heapq import heappush, heappop, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        
        heapify(stones)
        print(stones)
        while len(stones) > 1:
            fHeavy = heappop(stones)
            sHeavy = heappop(stones)
            
            if fHeavy != sHeavy:
                heappush(stones, fHeavy - sHeavy)
        if stones:
            return -heappop(stones)
        else:
            return 0
            
