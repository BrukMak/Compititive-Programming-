class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        N = len(nums)
        preSum = 0
        ans = len(nums)
        start = 0
        for i in range(N):
            preSum += nums[i]
            while preSum >= target:
                ans = min(ans, i - start + 1)
                preSum -= nums[start]
                start += 1
                
        
        return ans
            
                
            
            
            
            