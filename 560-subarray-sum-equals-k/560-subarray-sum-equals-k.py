class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        runningSum = defaultdict(int)
        runningSum[0] = 1
        res, cur = 0, 0
        for num in nums:
            cur += num
            if cur - k in runningSum:
                res += runningSum[cur - k]
            runningSum[cur] += 1
        return res
        
            
                    
            