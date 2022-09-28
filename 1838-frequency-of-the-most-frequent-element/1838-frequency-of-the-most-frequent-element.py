class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        window = 0
        l = 0
        preSum = [0]
        for i in range(N):
            preSum.append(preSum[i] + nums[i])
        
        for r in range(N):
            cost = nums[r] * (r - l + 1) - (preSum[r+1] - preSum[l])
            if k >= cost:
                window = max(window, r - l + 1)
            else:
                l += 1
        return window