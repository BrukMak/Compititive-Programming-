from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        count = 0
        queue = deque()
        di = dict()
        visited = set()
        visited.add(0)
        queue.append(0)
        
        for i in range(len(arr)):
            if arr[i] in di:
                di[arr[i]].append(i)
            else:
                di[arr[i]] = [i]
        print(di)
        while queue:
            size = len(queue)
            
            for _ in range(size):
                cur_i = queue.popleft()
                if cur_i == len(arr) - 1:
                    return count
                if cur_i - 1 >= 0 and  cur_i -1 not in visited:
                    visited.add(cur_i - 1)
                    queue.append(cur_i - 1)
                    
                if cur_i + 1 < len(arr) and  cur_i + 1 not in visited:
                    visited.add(cur_i + 1)
                    queue.append(cur_i + 1)
                    
                for i in range(len(di[arr[cur_i]])):
                    if di[arr[cur_i]][i] not in visited:
                        visited.add(di[arr[cur_i]][i])
                        queue.append(di[arr[cur_i]][i])
                    
                di[arr[cur_i]] = []
                
            count += 1
            
        