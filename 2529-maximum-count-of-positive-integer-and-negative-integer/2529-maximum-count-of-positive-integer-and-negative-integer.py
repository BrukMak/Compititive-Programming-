class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        zero = nums.count(0)
        l, r =0, len(nums)-1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] >= 0:
                r = mid - 1
            else:
                l = mid + 1
        return max(r+1, len(nums) - l - zero)