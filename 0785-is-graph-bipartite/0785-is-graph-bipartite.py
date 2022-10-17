class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        def dfs(node):
            
            if color[node] == -1: color[node] = 1
                
            for i in graph[node]:
                if color[i] == -1:
                    color[i] = 1 - color[node]
                    if not dfs(i):
                        return False
                else:
                    if color[i] == color[node]:
                        return False
            return True
                    
            
        for i in range(len(graph)):
            if color[i] == -1:
                if not dfs(i):
                    return False
        return True
            
        
        