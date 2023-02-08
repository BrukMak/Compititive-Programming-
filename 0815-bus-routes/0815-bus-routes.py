class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        for i, stops in enumerate(routes):
            for stop in stops:
                graph[stop].append(i)
        q = deque()
        q.append((source, 0))
        visited = set([source])
        while q:
            size = len(q)
            for _ in range(size):
                cur_node, group = q.popleft()
                if cur_node == target:
                    return group
                for i in range(len(graph[cur_node])):
                    for stop in routes[graph[cur_node][i]]:
                        if stop not in visited:
                            visited.add(stop)
                            q.append((stop, group +1))
                        routes[graph[cur_node][i]] = []
        return -1
        