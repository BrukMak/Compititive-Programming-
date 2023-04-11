class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        color = [0 for _ in range(n+1)] 
        graph = defaultdict(list)
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        
        
        def dfs(node, cur):
            if color[node] == 0:
                color[node] = cur
            visited.add(node)
            for child in graph[node]:
                if color[child] == color[node]:
                        return False
                if child not in visited:
                    color[child] = -cur
                    if not dfs(child, -cur):
                        return False
            return True
        visited = set()
        for i in range(1, n+1):
            if color[i] == 0:
                # visited.add(i)
                if not dfs(i, 1):
                    return False
        return True



            