class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)
        for i in range(len(color)):
            if color[i] == 0:
                if not self.bfs(graph, color, i):
                    return False
        return True
        
    
    def bfs(self, graph, color, node):
        
        que = deque()
        que.append(node)
        # color[node] = 1
        while que:
            size = len(que)
            current = que.popleft()
            if color[current] == 0:
                color[current] = 1
            for _ in range(size):
                for neighbour in graph[current]:
                    if color[neighbour] == 0:
                        color[neighbour] = -color[current]
                        que.append(neighbour)
                    else:
                        if color[neighbour] == color[current]:
                            return False
        return True
        