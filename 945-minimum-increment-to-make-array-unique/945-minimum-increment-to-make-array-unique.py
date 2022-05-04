class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        move = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                dif = (nums[i-1] - nums[i] + 1)
                move += dif
                nums[i] += dif
            
        return move
            
        