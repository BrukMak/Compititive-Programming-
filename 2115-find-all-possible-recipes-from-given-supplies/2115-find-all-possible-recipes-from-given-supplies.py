class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        req = defaultdict(int)
        supplies = set(supplies)
        for i, ing in enumerate(ingredients):
            for j in ing:
                if j in supplies or j in recipes:
                    graph[j].append(recipes[i]) 
                req[recipes[i]] += 1
                if j not in req:
                    req[j] = 0
        q = deque()
        ans = []
        for k, v in req.items():
            if v == 0: q.append(k)
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                
                for ne in graph[cur]:
                    req[ne] -= 1
                    if req[ne] == 0:
                        ans.append(ne)
                        q.append(ne)
        return ans
                        
            