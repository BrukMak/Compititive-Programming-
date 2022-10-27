class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # dist = [[float('inf')] * numCourses for _ in range(numCourses)]
        # for k in range(len(prerequisites)):
        #     i, j = prerequisites[k]
        #     dist[i][j] = 1
        # for k in range(numCourses):
        #     for i in range(numCourses):
        #         for j in range(numCourses):
        #             dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        # ans = []
        # for q in queries:
        #     i, j = q[0], q[1]
        #     ans.append(dist[i][j] != float('inf')) 
        # return ans
        
        graph = defaultdict(list)
        for p in prerequisites:
            i, j = p[0], p[1]
            graph[i].append(j)
        ans = []
        for q in queries:
            i, j = q[0], q[1]
            
            ans.append(self.dfs(j, i, graph, set()))
        return ans
    def dfs(self, start, i, graph, visited):
        # state = (i, start)
        # if state in memo:
            # return memo[state]
        if i == start:
            # memo[state] = True
            return True
        if i in visited:
            # memo[state] = False
            return False
        visited.add(i)
        
        for neighbour in graph[i]:
            if self.dfs(start, neighbour, graph, visited):
                return True
            
            
            
            