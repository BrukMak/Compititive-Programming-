class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        cur_sum = sum(nums)
        target_sum = N * (N + 1) // 2
        return target_sum - cur_sum