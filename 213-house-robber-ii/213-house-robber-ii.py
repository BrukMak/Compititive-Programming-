class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def dp(idx, num):
            if idx >= len(num):
                return 0
            if idx in memo:
                return memo[idx]
            memo[idx] = max(dp(idx+2, num) + num[idx], dp(idx + 1, num))
            return memo[idx]
        path1 = dp(1, nums)
        memo = {}
        nums = nums[:len(nums)-1]
        path2 = dp(0, nums)
        
        
        return max(path1, path2)
        