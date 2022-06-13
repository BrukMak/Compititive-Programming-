class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        res = []
        N = len(security)
        days_before , days_after = [0]*N, [0]*N
        for idx in range(1, N):
            days_before[idx] += days_before[idx-1] + 1 if security[idx-1] >= security[idx] else 0
                
        for idx in range(N-2, -1, -1):
            days_after[idx] += days_after[idx+1]+1 if security[idx+1]>= security[idx] else 0
        
        for i in range(N):
            if days_before[i] >= time and days_after[i] >= time:
                res.append(i)
        return res
            
                