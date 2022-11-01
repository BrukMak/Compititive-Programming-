class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        positive = self.helper(0, 1, True, nums, {})
        negative = self.helper(0, 1, False, nums, {})
        
        return max(positive, negative) + 1
    
    def helper(self, prev, index, flag, nums, memo):
        state = (prev, index, flag)
        if state in memo:
            return memo[state]
        
        if index >= len(nums):
            return 0
        take = 0
        skip = 0
        if (flag and nums[index] > nums[prev]) or (not flag and nums[index] < nums[prev]):
            take = 1 + self.helper(index, index + 1, not flag, nums, memo)
        skip = self.helper(prev, index + 1, flag, nums, memo)
        memo[state] = max(take, skip)
        return max(take, skip)
            