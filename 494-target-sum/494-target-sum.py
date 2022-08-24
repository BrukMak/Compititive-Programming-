class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def ts(idx, target):
            if (idx, target) in memo:
                return memo[(idx, target)]
            if idx >= len(nums):
                return target == 0
            add = ts(idx + 1, target+nums[idx])
            sub = ts(idx+1, target-nums[idx])
            memo[(idx, target)] = add + sub
            return memo[(idx, target)]
        return ts(0,target)