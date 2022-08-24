class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def ts(idx, target):
            if idx >= len(nums):
                return target == 0
            add = ts(idx + 1, target+nums[idx])
            sub = ts(idx+1, target-nums[idx])
            return add + sub
        return ts(0,target)