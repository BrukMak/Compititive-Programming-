class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = [-1]*len(nums)
        def dp(idx, num):
            if idx >= len(num):
                return 0
            if memo[idx] != -1:
                return memo[idx]
            memo[idx] = max(dp(idx+2, num) + num[idx], dp(idx + 1, num))
            return memo[idx]
        path1 = dp(1, nums)
        memo = [-1]*len(nums)
        nums = nums[:len(nums)-1]
        path2 = dp(0, nums)
        
        
        return max(path1, path2)
        