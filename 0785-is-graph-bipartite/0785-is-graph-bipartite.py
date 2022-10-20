class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # color = [-1] * len(graph)
        color = [0] * len(graph) # Number of node
        def checkBipartite(node, cur):
            if color[node] == 0: 
                color[node] = cur

            for neighbour in graph[node]:
                if color[neighbour] == 0:
                    color[neighbour] = -cur
                    
                    if not checkBipartite(neighbour, -cur):
                        return False
                elif color[node] == color[neighbour]:
                    return False

            return True
                    
            
        for i in range(len(graph)):
            if color[i] == 0:
                if not checkBipartite(i, 1):
                    return False
        return True
            
        
        