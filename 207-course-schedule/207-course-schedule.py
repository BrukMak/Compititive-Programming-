class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        inDegree = [0] * numCourses
        outgoing = defaultdict(set)
        queue = deque()
        count = 0
        
        for course, pre in prerequisites:
            outgoing[pre].add(course)
            inDegree[course] += 1
        
        
        for idx in range(numCourses):
            if inDegree[idx] == 0:
                queue.append(idx)
                
        while queue:
            cur = queue.popleft()
            count += 1
            for neighbour in outgoing[cur]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
                    
        return count == numCourses
                
            