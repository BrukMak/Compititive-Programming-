class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(set)
        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i][0], bombs[i][1], bombs[i][2]
            for j in range(len(bombs)):
                x2, y2, r2 = bombs[j][0], bombs[j][1], bombs[j][2]
                
                dist = sqrt((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2))
                if dist <= r1:
                    graph[i].add(j)
        
        def dfs(i):
            visited.add(i)
            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei)
            
        ans = 0
        for i in graph.keys():
            visited = set()
            dfs(i)
            ans = max(ans,len(visited))
        return ans