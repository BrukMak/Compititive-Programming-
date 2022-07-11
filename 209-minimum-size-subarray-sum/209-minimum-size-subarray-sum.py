class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        N = len(nums)
        preSum , start = 0, 0
        ans = float('inf')
        
        for i in range(N):
            preSum += nums[i]
            while preSum >= target:
                ans = min(ans, i - start + 1)
                preSum -= nums[start]
                start += 1
                
        
        return 0 if ans == float('inf') else ans
            
                
            
            
            
            