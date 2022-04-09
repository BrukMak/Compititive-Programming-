class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        safe = set()
        ans = []
        def dfs(node):
            if node in safe: return True
            if node in cycle: return False
            
            if node in visited:
                cycle.add(node)
                return False
            visited.add(node)
            
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    cycle.add(neighbour)
                    return False
            
            safe.add(node)
            return True
        
        for i in range(len(graph)):
            
            if dfs(i): ans.append(i)
                    
        return ans
                