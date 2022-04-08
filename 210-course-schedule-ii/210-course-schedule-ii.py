class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, visited = defaultdict(list), [0] * numCourses
        ans = []
        white = 0
        grey = 1
        black = 2
        for i in range(numCourses):
            graph[i] = []
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        def dfs(node):
            flag = True
            visited[node] = grey
            if node in graph:
                for neighbour in graph[node]:
                    if visited[neighbour] == white:
                        flag = dfs(neighbour) 
                    elif visited[neighbour] == grey:
                        return False
                    if not flag:
                        return flag
                    
            ans.append(node)
            visited[node] = black
            return True
        for key in graph:
            if visited[key] == white:
                if not dfs(key):
                    return []
        return ans[::-1]
            
            
        