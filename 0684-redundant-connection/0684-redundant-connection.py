class Solution:

    def makeSet(self, n):
        parent = [0] * (n + 1)
        size = [1] * (n+1)
        for i in range(1, n+1):
            parent[i] = i
        
        return parent, size
    
    def find(self, x, parent):
        if parent[x] != x:
            parent[x] = self.find(parent[x], parent)
        
        return parent[x]
    
    def union(self, x, y, parent,size):
        parentx = self.find(x, parent)
        parenty = self.find(y, parent)
        if parentx == parenty:
            return [x, y]
        
        if size[parentx] < size[parenty]:
            parentx, parenty = parenty, parentx
        
        parent[parenty] = parentx
        size[parentx] += size[parenty]
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent, size = self.makeSet(n)
        
        for x, y in edges:
            ans = self.union(x, y, parent, size)
            if ans: 
                return ans