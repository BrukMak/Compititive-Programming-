class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        ans = 0
        l = 0
        max_count = 0
        max_val = max(nums)
        for r in range(len(nums)):
            if nums[r] == max_val:
                max_count += 1
            while max_count >= k:
                ans += 1 + len(nums) - (r + 1)
                if nums[l] == max_val:
                    max_count -= 1
                l += 1
        
        return ans