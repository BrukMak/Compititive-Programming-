class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [0] * len(isConnected)
        size = [0] * len(isConnected)
        def make_set(v):
            parent[v] = v
            size[v] = 1
        
        def find(v):
            if v == parent[v]:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(n1, n2):
            a = find(n1)
            b = find(n2)
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
        
        for i in range(len(isConnected)):
            make_set(i)
        for row in range(len(isConnected)):
            for col in range(len(isConnected)):
                if row != col and isConnected[row][col] == 1:
                    union(row, col)         
        for i in range(len(parent)):
            find(i)
        return len(set(parent))
                    
                
            