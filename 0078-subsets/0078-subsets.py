class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        def dfs(idx, arr):
            if idx >= N:
                ans.append(arr[:])
                return
            
            dfs(idx + 1, arr + [nums[idx]])
            dfs(idx + 1, arr)
        ans = []
        dfs(0, [])
        return ans