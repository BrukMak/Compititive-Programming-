class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        que = deque()
        que.append([N-1, nums[N-1]])
        
        for i in range(N-2, -1, -1):
            cur  = que[-1][1] + nums[i]
            
            while que and cur >= que[0][1]:
                que.popleft()
                
            que.appendleft([i,cur])
            
            while que[-1][0] - que[0][0] + 1 > k:
                que.pop()
                
        return que[0][1]