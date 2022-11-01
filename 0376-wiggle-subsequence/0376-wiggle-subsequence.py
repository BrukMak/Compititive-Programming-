class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        @cache
        def helper(prev, index, flag):
            # state = (prev, index, flag)
            # if state in memo:
            #     return memo[state]

            if index >= len(nums):
                return 0
            take = 0
            skip = 0
            if (flag and nums[index] > nums[prev]) or (not flag and nums[index] < nums[prev]):
                take = 1 + helper(index, index + 1, not flag)
            skip = helper(prev, index + 1, flag)
            # memo[state] = max(take, skip)
            return max(take, skip)
        
        positive = helper(0, 1, True)
        negative = helper(0, 1, False)
        
        return max(positive, negative) + 1
            