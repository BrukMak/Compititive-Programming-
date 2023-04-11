class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        def dfs(node, path):
            if node == n-1:
                ans.append(path[:])
                return
            
            for nei in graph[node]:
                dfs(nei, path + [nei])
        dfs(0, [0])
        return ans
            