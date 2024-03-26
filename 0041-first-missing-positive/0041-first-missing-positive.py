class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        nums = set(nums)
        for i in range(1, N + 2):
            if i not in nums:
                return i
        