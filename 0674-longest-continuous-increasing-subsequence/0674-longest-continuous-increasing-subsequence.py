class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        current_res = 0
        for i in range(len(nums)):
            if i != 0 and nums[i-1] < nums[i]:
                current_res += 1
            else:
                current_res = 1
            
            res = max(res, current_res)
        return res