from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        visited = set()
        visited.add(start)
        queue.append(start)
        
        while queue:
            size = len(queue)
            for _ in range(size):
                cur_i = queue.popleft()
                if arr[cur_i] == 0:
                    return True
                if cur_i - arr[cur_i] >=0 and cur_i - arr[cur_i] not in visited:
                    visited.add(cur_i - arr[cur_i])
                    queue.append(cur_i - arr[cur_i])
                if cur_i + arr[cur_i]  < len(arr) and cur_i + arr[cur_i]  not in visited:
                    visited.add(cur_i + arr[cur_i])
                    queue.append(cur_i + arr[cur_i])
        return False
                    
            
            