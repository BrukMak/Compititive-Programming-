class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        # Sliding window with hash table
        ans = 0
        freq = {}
        l = 0
        for r in range(len(nums)):
            if nums[r] in freq:
                freq[nums[r]] += 1
            else:
                freq[nums[r]] = 1
            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        
        return ans
                