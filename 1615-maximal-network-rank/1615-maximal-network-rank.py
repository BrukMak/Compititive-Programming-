class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        #Degree calculation
        degree = defaultdict(int)
        for s, d in roads:
            degree[s] += 1
            degree[d] += 1
        
        #Finding the maximum road between neighbouring nodes
        maxRoad = 0
        
        #Quick check is the road exist b/n pair of nodes
        pairs = {tuple(pair) for pair in roads}
            
        for i in range(n):
            for j in range(i+1, n):
                if (i, j) in pairs or (j, i) in pairs:
                    maxRoad = max(maxRoad, degree[i] + degree[j] - 1)
                else:
                    maxRoad = max(maxRoad, degree[i] + degree[j])
                
        
        return maxRoad
