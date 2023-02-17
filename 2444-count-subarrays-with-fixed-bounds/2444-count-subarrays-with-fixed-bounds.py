class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
            
        l = 0
        min_index = -1
        max_index = -1
        ans = 0
        
        for r, val in enumerate(nums):
            if val < minK or val > maxK:
                l = r + 1
            else:
                if val == minK:
                    min_index = r
                if val == maxK:
                    max_index = r
                if l <= min_index and l <= max_index:
                    ans += min(min_index, max_index) - l + 1
        return ans