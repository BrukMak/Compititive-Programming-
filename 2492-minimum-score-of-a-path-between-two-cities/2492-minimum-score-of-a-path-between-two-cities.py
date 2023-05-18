class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]
        for start, end, weight in roads:
            self.union(start, end)
        self.parent
        ans = math.inf
        for start, end, weight in roads:
            if self.isConnected(n, start):
                ans = min(ans, weight)
        return ans
        
    def find(self, val):
        if self.parent[val] != val:
            self.parent[val] = self.find(self.parent[val])
        return self.parent[val]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        
        if parent_x != parent_y:
            if self.size[parent_x] < self.size[parent_y]:
                parent_x, parent_y = parent_y, parent_x
            self.parent[parent_y] = parent_x
            self.size[parent_x] += self.size[parent_y]
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)