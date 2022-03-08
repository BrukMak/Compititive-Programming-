class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        size = len(senate)
        while queue:
            cur = queue.popleft()
            if cur == 0:
                continue
            ptr = 0
            
            while (ptr < len(queue)) and (queue[ptr] == cur or queue[ptr] == 0):
                ptr += 1  
                
            if ptr < len(queue):
                queue[ptr] = 0
                queue.append(cur)
            else:
                queue.appendleft(cur)
                break
        return "Dire" if queue[0] == "D" else "Radiant"

                