class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        visited = set()
        
        for n1, n2 in adjacentPairs:
            graph[n1].add(n2)
            graph[n2].add(n1)
        for k, v in graph.items():
            if len(v) == 1:
                start = k
                break
        ans = []
        visited = set()
        self.dfs(start, ans, visited, graph)
        return ans
            
    def dfs(self, node, ans, visited, graph):
        if node in visited:
            return
        ans += [node]
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                self.dfs(child, ans, visited, graph)
        return ans
        