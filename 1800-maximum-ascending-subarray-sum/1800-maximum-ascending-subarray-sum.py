class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        running_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                running_sum = nums[i]
            else:
                running_sum += nums[i]
            max_sum = max(max_sum, running_sum)
        return max_sum
