class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        
        
        @lru_cache(None)
        def helper(index, target, length):
            if target < 0:
                return False
            if index == n:
                return target == 0 and length == 0
            # if index + length > n or target < 0:
            #     return False
            
            return helper(index + 1, target - nums[index], length - 1) or helper(index + 1, target, length)
        
        for length in range(1, n):
            if (s * length) % n == 0 and helper(0, (s * length) // n, length):
                return True
        return False
