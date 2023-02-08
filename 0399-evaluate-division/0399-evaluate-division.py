class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(dict)
        
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1 / values[i]
        result = []
        for node1, node2 in queries:
            result.append(self.dfs(node1, node2, set(), graph))
        
        return result
        
    def dfs(self, node1, node2, visited, graph):
        if node1 not in graph or node2 not in graph:
            return -1

        if node2 in graph[node1]:
            return graph[node1][node2]

        for child in graph[node1]:
            if child not in visited:
                visited.add(child)
                cur = self.dfs(child, node2, visited, graph)
                if cur != -1:
                    return cur * graph[node1][child]
        return -1