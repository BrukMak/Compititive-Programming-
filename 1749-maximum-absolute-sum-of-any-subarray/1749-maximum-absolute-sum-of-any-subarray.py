class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        max_sum = float('-inf')
        min_sum = float('inf')
        max_sum_here = 0
        min_sum_here = 0
        
        for i in range(len(nums)):
            max_sum_here += nums[i]
            min_sum_here += nums[i]
            max_sum = max(max_sum, max_sum_here)
            min_sum = min(min_sum, min_sum_here)
            if max_sum_here < 0:
                max_sum_here = 0
            if min_sum_here > 0:
                min_sum_here = 0
        return max(abs(max_sum), abs(min_sum))