class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, tar):
            if (i, tar) in memo:
                return memo[(i, tar)]
            if tar == target:
                memo[(i, tar)] = 1
                return memo[(i, tar)]
            if tar > target:
                memo[(i, tar)] = 0
                return memo[(i, tar)]
            count = 0
            for idx in range(len(nums)):
                
                count += dp(idx, tar + nums[idx])
            memo[(i, tar)] = count
            return count
            
        
        return dp(0, 0)