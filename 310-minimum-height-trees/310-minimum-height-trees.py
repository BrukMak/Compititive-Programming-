class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj_list = defaultdict(set)
        for f, s in edges:
            adj_list[f].add(s)
            adj_list[s].add(f)
            
        queue = []
        for key in adj_list:
            if len(adj_list[key]) == 1:
                queue.append(key)
        
        while len(adj_list) > 2:
            new_q = []
            for item in queue:
                temp = adj_list[item].pop()
                del adj_list[item]
                adj_list[temp].remove(item)
                if len(adj_list[temp]) == 1:
                    new_q.append(temp)
            queue = new_q
            
        return queue
                
        