class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR with each elemet in the array
        # XOR 0 - N 
        # XOR the two results
        res = len(nums)
        for i in range(len(nums)):
            res ^= nums[i]
            res ^= i
        return res