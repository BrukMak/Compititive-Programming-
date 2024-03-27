class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        count = 0
        score = 0
        l = 0
        for r in range(len(nums)):
            score += nums[r]
            
            while score * (r-l+1) >= k:
                score -= nums[l]
                l += 1
            count += (r-l+1)
            
        return count