class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_cost = 0
        size = len(points)
        graph = defaultdict(list)
        for i in range(size):
            x1, y1 = points[i]
            for j in range(1, size):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                graph[j].append([dist, i])
                graph[i].append([dist, j])
        visited = set()
        min_heap = [[0,0]]
        
        while len(visited) < size:
            cost , node = heappop(min_heap)
            if node in visited:
                continue
            min_cost += cost
            visited.add(node)
            for neiCost, nei in graph[node]:
                if nei not in visited:
                    heappush(min_heap, [neiCost, nei])
            
        return min_cost
            