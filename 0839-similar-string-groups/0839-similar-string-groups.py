class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def check(string1, string2):
            char_diff = 0
            for i in range(len(string1)):
                if string1[i] != string2[i]:
                    char_diff += 1
            return char_diff <= 2

        def bfs(node, index, visited, strs):
            que = deque()
            que.append(node)
            visited.add(node)

            while que:
                size = len(que)
                for _ in range(size):
                    cur = que.popleft()
                    for j in range(index + 1, len(strs)):
                        string2 = strs[j]
                        if string2 not in visited and check(cur, string2):
                            que.append(string2)
                            visited.add(string2)

    
        N = len(strs)
        visited = set()
        answer = 0
        for index, s in enumerate(strs):
            if s not in visited:
                bfs(s,index, visited, strs)
                answer += 1
        return answer
        