class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [0 for _ in range(n+1)] 
        graph = defaultdict(list)
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
            
        for i in range(1, n+1):
            if color[i] == 0:
                q = deque()
                q.append(i)
                color[i] = 1
                while q:
                    curr_node = q.pop()
                    cur_color = color[curr_node]
                    for child in graph[curr_node]:
                        if color[child] == 0:
                            color[child] = -1 * cur_color
                            q.append(child)
                        elif color[child] == color[curr_node]:
                            return False
        return True
            