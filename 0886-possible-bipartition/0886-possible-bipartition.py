class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [0 for _ in range(n+1)] 
        graph = defaultdict(list)
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node, cur_color, ans):
            if color[node] == 0:
                color[node] = cur_color
            visited.add(node)
            for child in graph[node]:
                if color[child] == color[node]:
                        return False
                if child not in visited:
                    ans = ans and dfs(child, -cur_color, ans)
            return ans
        visited = set()
        for i in range(1, n+1):
            if color[i] == 0:
                # visited.add(i)
                if not dfs(i, 1, True):
                    return False
        return True



            