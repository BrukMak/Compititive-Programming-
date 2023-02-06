class Solution:
    def racecar(self, target: int) -> int:
        q = deque()
        q.append((0, 0, 1))
        visited = set()
        while q:
            count, pos, speed = q.popleft()
            
            if pos == target:
                return count
            
            if (pos, speed) in visited:
                continue
            
            q.append((count + 1, pos + speed, 2 * speed))
            
            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                speed = -1 if speed > 0 else 1
                q.append((count + 1, pos, speed))
            