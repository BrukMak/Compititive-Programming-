class Solution:
    def findMaxSubarraySum(self, nums):
        # Fiding the maximum subarray using kadane's algorithm
        max_so_far = float('-inf')
        max_ending_here = 0
        
        for num in nums:
            max_ending_here += num
            max_so_far = max(max_so_far, max_ending_here)
            if max_ending_here < 0:
                max_ending_here = 0
        
        return max_so_far
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        
        full_array_result = self.findMaxSubarraySum(nums)
        
        sufix = ([0] * (n-1)) + [nums[n-1]]
        suf_sum = nums[n-1]
        for i in range(n-2, -1, -1):
            suf_sum += nums[i]
            sufix[i] = max(suf_sum, sufix[i+1])
        
        pre_sum = nums[0]
        prefix = nums[0]
        split_sum = float('-inf')
        for i in range(1, len(nums)):
            pre_sum += nums[i]
            prefix = max(prefix, pre_sum)
            if i < n-1:
                split_sum = max(split_sum, prefix + sufix[i+1])
        return max(split_sum, full_array_result)