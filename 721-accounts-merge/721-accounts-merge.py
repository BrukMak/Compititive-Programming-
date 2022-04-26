class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [0] * len(accounts)
        size = [0] * len(accounts)
        visited = defaultdict(int)
        def make_set(v):
            parent[v] = v
            size[v] = 1
            
        def find(val):
            if parent[val] != val:
                parent[val] = find(parent[val])
            return parent[val]
        
        def union(x, y):
            a = find(x)
            b = find(y)
            if a != b:
                if size[a] < size[b]:
                    a, b = b , a
                parent[b] = a
                size[a] += size[b]
        for i in range(len(accounts)):
            make_set(i)
        for row in range(len(accounts)):
            for col in range(1, len(accounts[row])):
                if accounts[row][col] in visited:
                    row_of_the_visited = visited[accounts[row][col]]
                    
                    union(row_of_the_visited, row)
                else:
                    visited[accounts[row][col]] = row
        cur = 0
        ans = []
        temp_ans = []
        for i in range(len(accounts)):
            find(i)
        while cur < len(accounts):
            for i in range(len(accounts)):
                if parent[i] == cur:
                    for it in accounts[i]:
                        temp_ans.append(it)
            if temp_ans:
                name = temp_ans[0]
                temp_ans = list(set(temp_ans))
                temp_ans.remove(name)
                temp_ans.sort()
                temp_ans = [name] + temp_ans 
                ans.append(temp_ans)
                temp_ans = []
            cur += 1
        
        return ans
            
                
                
                
        
        