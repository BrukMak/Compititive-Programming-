class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        move = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                move += (nums[i-1] - nums[i] + 1)
                nums[i] += (nums[i-1] - nums[i] + 1)
            
        return move
            
        