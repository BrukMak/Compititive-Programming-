class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w,v))
        minHeap = []
        heappush(minHeap, (0, k))
        dist = [float('inf')] * n
        visited = set()
        while minHeap:
            curW, curNode = heappop(minHeap)
            visited.add(curNode)
            
            if dist[curNode-1] != float('inf'):
                continue
            dist[curNode-1] = curW
            if len(visited) == n:
                break
            for child in graph[curNode]:
                w, node = child
                newW = curW + w
                heappush(minHeap, (newW, node))
        res = max(dist)
        return res if res != float('inf') else -1
