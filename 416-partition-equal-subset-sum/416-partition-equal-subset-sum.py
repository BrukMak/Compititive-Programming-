class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        @lru_cache(None)
        def subsequenceFinder(idx, half):
            if idx >= len(nums) : return half == 0
            
            return  subsequenceFinder(idx+1, half - nums[idx]) or subsequenceFinder(idx+1, half)
        
        return subsequenceFinder(0, total // 2) if total % 2 == 0 else False