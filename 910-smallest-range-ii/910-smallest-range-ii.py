class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_val = nums[-1]
        min_val = nums[0]
        ans = max_val - min_val
        size = len(nums)
        
        for i in range(size - 1):
            if nums[i] < nums[i + 1]:
                max_val = max(nums[-1] - k, nums[i] + k)
                min_val = min(nums[0] + k, nums[i + 1] - k)
                ans = min(ans, max_val - min_val)
        return ans