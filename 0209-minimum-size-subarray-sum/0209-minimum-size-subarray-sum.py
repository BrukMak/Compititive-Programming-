class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        windowSize = float('inf')
        windowSum = 0
        left = 0
        for right in range(n):
            windowSum += nums[right]
            
            while windowSum >= target:
                windowSize = min(windowSize, right - left + 1)
                windowSum -= nums[left]
                left += 1
                
        return windowSize if windowSize < float('inf') else 0