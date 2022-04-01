class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        def lis(idx):
            if idx == n:
                return 0
            if memo[idx] != -1:
                return memo[idx]
            cur_max = 0
            for i in range(idx, len(nums)):
                if nums[i] > nums[idx]:
                    cur_max = max(cur_max, lis(i))
                    
            memo[idx] = cur_max + 1
            return memo[idx]
        for i in range(len(nums)):
            lis(i)
        
        return max(memo) 