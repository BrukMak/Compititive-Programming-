class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        visited = set()
        graph = defaultdict(list)
        #make the graph
        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)
        
        res = [*s]
        #traverse through all the connected edges and add the character and the idices to the respective list
        def dfs(i):
            chars.append(s[i])
            idx.append(i)
            visited.add(i)
            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei)
        # call the dfs for un-visited nodes in the graph
        for i in graph.keys():
            if i not in  visited:
                chars = []
                idx = []
                dfs(i)
                chars.sort()
                idx.sort()
                for i in range(len(idx)):
                    res[idx[i]] = chars[i]
        return "".join(res)
                
                
            
            
            