class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            count = 0
            mid = l + (r-l) // 2
            
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count > mid:
                r = mid
            else:
                l = mid + 1
        return l
