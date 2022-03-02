class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        def dfs(idx):
            for col in range(len(isConnected)):
                if isConnected[idx][col] == 1 and col not in visited:
                    visited.add(col)
                    dfs(col)
                
            return 
        for idx in range(len(isConnected)):
            if idx not in visited:
                visited.add(idx)
                dfs(idx)
                count += 1
        return count
