class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        result = 0
        prod = 1
        l = 0
        for r in range(len(nums)):
            prod *= nums[r]
            while l < r and prod >= k:

                prod //= nums[l]
                l += 1
                
                if l == len(nums):
                    return result
            if prod < k:
                window = r - l + 1
                result += window
        
        return result
                
                