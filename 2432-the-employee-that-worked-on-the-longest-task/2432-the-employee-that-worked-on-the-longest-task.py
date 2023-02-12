class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        
        prevTime = 0
        ans = [0, 0]
        for ID, delay in logs:
            currTime = delay - prevTime
            if currTime > ans[0]:
                ans = [currTime, ID]
            elif currTime == ans[0]:
                ans[1] = min(ans[1], ID)
            prevTime = delay
            
        return ans[1]
                