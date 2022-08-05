class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(i, tar):
            
            if tar == target:
                return 1
            if tar > target:
                return 0
            count = 0
            for idx in range(len(nums)):
                
                count += dp(idx, tar + nums[idx])
            return count
            
        
        return dp(0, 0)
            