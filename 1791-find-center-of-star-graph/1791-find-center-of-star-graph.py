class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        count = defaultdict(int)
        for u, v in edges:
            count[u] += 1
            count[v] += 1
            
            if count[u] > 1:
                return u
            if count[v] > 1:
                return v