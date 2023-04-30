class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left = 0
        right = max(nums) - min(nums)
        
        while left <= right:
            mid = (right + left) // 2
            if self.isPossible(mid, nums, p):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def isPossible(self, val, nums, p):
        count = 0
        i = 0
        while i < (len(nums)-1):
            if nums[i+1] - nums[i] <= val:
                i += 2
                count += 1
            else:
                i += 1
        return count >= p