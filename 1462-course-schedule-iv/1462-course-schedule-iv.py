class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dist = [[float('inf')] * numCourses for _ in range(numCourses)]
        for k in range(len(prerequisites)):
            i, j = prerequisites[k]
            dist[i][j] = 1
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        ans = []
        for q in queries:
            i, j = q[0], q[1]
            ans.append(dist[i][j] != float('inf')) 
        return ans