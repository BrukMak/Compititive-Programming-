class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        inDegree = [0]*numCourses
        outgoing = defaultdict(set)
        
        for course, pre in prerequisites:
            outgoing[pre].add(course)
            inDegree[course] += 1
        
        queue = deque()
        
        for idx in range(numCourses):
            if inDegree[idx] == 0:
                queue.append(idx)
        ans = []
        count = 0
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            count += 1
            for neighbour in outgoing[cur]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
        if count == numCourses:
            return ans
        return []