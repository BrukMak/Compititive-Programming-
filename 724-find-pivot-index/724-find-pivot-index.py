class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        pre = 0
        
        for i in range(len(nums)):
            post = sum_ - pre - nums[i]
            if pre == post:
                return i
            pre += nums[i]
        return -1