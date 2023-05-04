class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [0]
        for stone in stones:
            heappush(max_heap, -stone)
        while len(max_heap) > 1:
            first = - heappop(max_heap)
            second = - heappop(max_heap)
            diff = first - second
            if diff:
                heappush(max_heap, -diff)
        return -max_heap[0]
                
            