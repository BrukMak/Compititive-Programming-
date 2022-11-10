class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        color = [0] * N
        for node in range(N):
            if color[node] == 0:
                if not self.coloring(node, graph, color, 1):
                    return False
        return True
    # Color every node with alternating colors
    # if Neighbour of a node has same color return False
    def coloring(self, node, graph, color, cur_color):
        if color[node] == 0:
            color[node] = cur_color
            
        for neighbour in graph[node]:
            if color[neighbour] == 0:
                color[neighbour] = -cur_color
                if not self.coloring(neighbour, graph, color, -cur_color):
                    return False
            elif color[neighbour] == color[node]:
                return False
        return True
        
        