class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        def next_val(val):
            val1 = str((val + 1) % 10)
            val2 = str((val - 1)) if val > 0 else '9'
            return [val1, val2]
        
        def bfs(start):
            visited = set()
            que = []
            heappush(que, (0, start))
            visited.add(start)
            while que:
                cur = heappop(que)
                
                for i in range(4):
                    val_to_change = cur[1][i]
                    changed_vals = next_val(int(val_to_change))
                    candidate1 = cur[1][:i] + changed_vals[0] + cur[1][i+1:]
                    
                    if candidate1 not in deadends and candidate1 not in visited:
                        visited.add(candidate1)
                        heappush(que, (cur[0] + 1, candidate1))
                    candidate2 = cur[1][:i] + changed_vals[1] + cur[1][i+1:]
                    if candidate2 not in deadends and candidate2 not in visited:
                        heappush(que, (cur[0] + 1, candidate2))
                        visited.add(candidate2)
                    if candidate1 == target or candidate2 == target:
                        return cur[0]+1
            return -1        
        
        if "0000" in deadends: return -1
        return bfs("0000") if target != "0000" else 0
                    
                    
                    
                    