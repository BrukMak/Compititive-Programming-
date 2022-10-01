class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = float('-inf')
        cur = 0
        for i in range(len(nums)):
            cur = max(cur + nums[i], nums[i])
            res = max(res, cur)
        return res
        