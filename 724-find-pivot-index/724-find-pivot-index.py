class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = 0
        pre = 0
        for item in nums:
            sum_ += item
        for i in range(len(nums)):
            post = sum_ - pre - nums[i]
            if pre == post:
                return i
            pre += nums[i]
        return -1