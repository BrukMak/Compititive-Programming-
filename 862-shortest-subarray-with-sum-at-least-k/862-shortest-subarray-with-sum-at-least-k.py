class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        pre = [0]
        for i in range(N):
            pre.append(pre[-1] + nums[i])
            
        ans = N + 1
        q = deque()
        for i in range(N + 1):
                
            while q and pre[q[-1]] > pre[i]:
                q.pop()
            while q and pre[i] - pre[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            q.append(i)
            
        return ans if ans < N + 1 else -1
        
        