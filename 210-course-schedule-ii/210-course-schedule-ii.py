class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, visited = defaultdict(list), set() 
        ans = []
        cycle = set()
        safe = set()
        
        for i in range(numCourses):
            graph[i] = []
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        def dfs(node):
            if node in cycle: return False
            if node in safe: return True
            
            if node in visited:
                cycle.add(node)
                return False
            
            visited.add(node)
            
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    cycle.add(node)
                    return False
                    
            ans.append(node)
            safe.add(node)
            return True
        
        for key in graph:
            if not dfs(key):
                return []
            
        return ans[::-1]
            
            
        