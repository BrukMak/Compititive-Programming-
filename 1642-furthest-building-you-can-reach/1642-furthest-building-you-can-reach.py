from heapq import heappush,heappop
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []
        i = 0
        while i < len(heights) - 1 :
            
            if heights[i + 1] <= heights[i]:
                i += 1
                continue
                
            if heights[i + 1] - heights[i] <= bricks:
                bricks -= heights[i + 1] - heights[i]
                heappush(max_heap, - (heights[i + 1] - heights[i]))
            elif ladders:
                if max_heap:
                    top = -max_heap[0]
                    # print(top)
                    if top > (heights[i + 1] - heights[i]):
                        top = -heappop(max_heap)
                        bricks += (top - (heights[i + 1] - heights[i]))
                        heappush(max_heap, -(heights[i + 1] - heights[i]))
                ladders -= 1
            else:
                break
            i += 1
        return i