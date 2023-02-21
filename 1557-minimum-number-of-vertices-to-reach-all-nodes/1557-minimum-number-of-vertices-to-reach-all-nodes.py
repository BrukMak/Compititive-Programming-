class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        
        for source, dest in edges:
            indegree[dest] += 1
            
        ans = []
        for node in range(n):
            if indegree[node] == 0:
                ans.append(node)
        
        return ans