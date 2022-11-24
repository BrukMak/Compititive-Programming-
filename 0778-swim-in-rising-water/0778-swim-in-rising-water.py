import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
    
# def calc_elevation(grid):
        ROWS = len(grid)
        COLS = len(grid[0])

        heap = [(grid[0][0] , 0, 0)]
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        inbound = lambda r, c: 0 <= r < ROWS and 0 <= c < COLS
        visited = set()
        visited.add((0, 0))
        ans = 0

        while heap:
            #(time, i, j)l
            time, i, j = heapq.heappop(heap)

            if i == ROWS - 1 and j == COLS - 1:
                ans = time
                break

            for dx, dy in direction:
                nx, ny = i + dx, j + dy

                if not inbound(nx, ny) or (nx, ny) in visited:
                    continue

                if time >= grid[nx][ny]:
                    heapq.heappush(heap, (time, nx, ny))
                else:
                    heapq.heappush(heap, (grid[nx][ny], nx, ny))
                visited.add((nx, ny))

        return ans