class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @lru_cache(None)
        def dfs(nums):
            if nums == []: return 0
            
            res = 0
            for i in range(min(k,len(nums))):
                val = max(nums[:i+1]) * (i+1)
                cur  = dfs(nums[i+1:]) + val
                if cur > res:
                    res = cur
            return res
        return dfs(tuple(arr))
    