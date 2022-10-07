class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        def dfs(node, path):
            path.append(node)
            if node == n-1:
                ans.append(path.copy())
                return
            
            for nei in graph[node]:
                dfs(nei, path)
                path.pop()
        dfs(0, [])
        return ans
            