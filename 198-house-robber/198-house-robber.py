class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        memo = {}
        def dfs(idx):
            
            if idx >= houses:
                return 0
            if idx in memo: return memo[idx]
            memo[idx] = max(dfs(idx + 2) + nums[idx], dfs(idx + 1)) 
            return memo[idx]

        return dfs(0)